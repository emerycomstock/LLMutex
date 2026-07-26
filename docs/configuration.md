# Configuration Design

## Settings

...

## Resources

The best way to think about "resources" is to consider each resource a distinct piece of hardware, like a graphics card or even an entire server. For that resource, you can have multiple "sources" which are roughly the interfaces by which you can use that resource to interact with a model, like Ollama API or a CLI tool that invokes an image generation model. Each resource has some capacity for use based on its hardware specs and each source is capable of consuming some of that capacity depending on the model being used. The point of resources is to map out both that capacity and how use affects capacity to properly allocate resources that can handle the needs of queued consumers in a way that maximizes utilization.

## Configuration Models

Some important notes on configuration model types:
- Required fields should have valid defaults whenever possible, lowers chance of config rejection on load (especially for file sources)

## Configuration Sources

...

### File Configuration Source

The primary means (and source of truth) for configuration is going to be file sources. Initial values are read from the linked files and any other sources or overrides are applied directly to the file, turning it into a single source of truth for the relevant configuration. File configuration sources will similarly be checked for updates live at a pre-configured interval, enabling real-time updates.

#### Settings Files

Format and default values for `settings` file:
```yaml
# API layer config
api:
    http_port: 3440
    https_port: 6440
    # TODO: TLS config

# Leasing feature config
leasing:
    # NOTE: One of either "allow_leasing" or "allow_on_demand" must be true
    # Whether to allow lease requests, if false, "chat" and "generate" requests can only be made on-demand
    allow_leasing: true
    # Whether to allow on-demand requests, if false, "chat" and "generate" requests can only be made with a lease
    allow_on_demand: true

    lease_inactivity_timeout_s: 30

    duration_based_leasing:
        enabled: true
        # If true, default will be applied to leases where limit is not specified
        required: true
        # Whether the request that breaches this limit should be allowed to finish gracefully
        allow_final_request_overflow: true
        min_lease_duration_s: 1
        max_lease_duration_s: 3600 # 1 hour
        default_lease_duration_s: 600 # 10 minutes

    input_token_based_leasing:
        enabled: true
        # If true, default will be applied to leases where limit is not specified
        required: false
        # Whether the request that breaches this limit should be allowed to finish gracefully
        allow_final_request_overflow: true
        min_token_limit: 1
        max_token_limit: 65536 # 2^16
        default_token_limit: 16384 # 2^14
    
    output_token_based_leasing:
        enabled: true
        # If true, default will be applied to leases where limit is not specified
        required: false
        # Whether the request that breaches this limit should be allowed to finish gracefully
        allow_final_request_overflow: true
        min_token_limit: 1
        max_token_limit: 16384 # 2^14
        default_token_limit: 4096 # 2^12
        
```

#### Resource Files

Format and default values for `resources` file:
```yaml
resources:
    # Unique string id, used in API requests (slug, unique)
  - id_slug: example-resource
    # Display name for use by clients and future features
    display_name: "Example Resource"
    # List of providers
    providers:
        # Provider id, used in API requests (slug, unique)
      - id_slug: "example-api-provider"
        # Provider display name
        display_name: "Example API Provider"
        # TODO: CLI support
        # Currently supported values: [api]
        provider_type: api
        # Detail model dependent on provider type, example shows API type provider details
        provider_details:
            # TODO: More API spec support
            # API spec, currently supported values: [ollama]
            spec: ollama
            host: localhost
            port: 11434 # Ollama default port
            use_tls: false
            # TODO: TLS Config
    # TODO: Model access config, overrides, & concurrency settings
```

...

### File Configuration

...

### Env Overrides

...

### Label Overrides

...

### API Overrides

...
# LLMutex

**Version:** v0.1.0 *(alpha)* \
**State:** Not ready for use

A mutex-like API for leasing LLM resource access. The main purpose of this is to allow LLM self-hosters who lack personal basement datacenters to create LLM-powered applications that autonomously share access in uninterrupted blocks rather than request-by-request.

See `./docs/` for detailed design and release information.

## Features

### AuthN/AuthZ features

|Name|Description|Target|
|----|-----------|------|
|Consumer registration|Consumers that use the LLM through this service will be able to request API keys that they use to request and utilize leases on the resources|v1.0|
|Admin key|The service will generate an admin API key and print it to std out on startup|v1.0|

### Service state & configuration features

The service settings and available resource configuration will have multiple sources that ultimately merge into the designated config file as a single source of truth.

|Type|Name|Description|Target|
|----|----|-----------|------|
|Field|Maximum lease queue size|The maximum number of queued consumers before the service refuses to queue more consumers|v1.0|
|Field|Min & max lease period|The bounds within which a lease can be claimed|v1.0|
|Field|Lease inactivity timeout|Failing to use the LLM within the timeout period after last use will cause the lease to end early|v1.0|
|Field|Lease claim timeout|When a new lease owner is designated from the queue, they must claim their lease within the timeout|v1.0|
|Field|Config hot-reload interval|Interval at which the config will be checked for changes and re-applied|v1.0|
|Field|Maximum tokens per lease|Set a maximum token usage before lease terminates|TBD|
|Field|Maximum requests per lease|Set a maximum request count before lease terminates|TBD|
|Functionality|Configuration vending|Current server settings can be requested by consumers|v1.0|
|Functionality|LLM resource listing & status|Consumers can see a list of available resources including resource status, queue lengths, etc.|v1.0|
|Functionality|YAML-based configuration|A single YAML-based config file will define service settings and available LLM resources|v1.0|
|Functionality|Default config|If no configuration file exists on startup an initial configuration file will be generated with pre-configured defaults|v1.0|
|Functionality|Env variable overrides|Env variables will be checked for configuration overrides and applied to the configuration file on startup|TBD|
|Functionality|API overrides|At runtime, API requests to alter configuration files will result in those overrides being applied to the configuration file in its current state|TBD|
|Functionality|Label-based settings & resource discovery|Allow use of docker labels to register/discover LLM resources not specified in config|TBD|

Order of application for configuration sources (later ones override earlier ones):
```
1. Default values
2. Configuration file initial content
3. Env variables
4. Label-based overrides
5. API overrides
```

*Source of truth will always be the configuration file itself, env variables and API requests will overwrite content of configuration file and force re-application.*

### Leasing features

Leasing resources is the service's primary function, this allows consumers (designated by their service-vended API keys) to monopolize a resource for a given time or set amount of usage.

|Name|Description|Target|
|----|-----------|------|
|Time-based leasing|Consumers can request a lease on a resource for a designated period of time where they are guaranteed access|v1.0|
|Token-based leasing|Set a maximum token usage before lease terminates|TBD|
|Count-based leasing|Set a maximum request count before lease terminates|TBD|
|On-demand leasing|Make a request without a lease, automatically queues a lease with a max count of 1 and the request|TBD|
|Web hook notifications|When a lease starts and ends, utilize web hooks to optionally notify consumers|TBD|
|Leasing queue|When a resource cannot be obtained, the requester will be added to queue to obtain the lease|v1.0|
|Request queue|Allow consumers who have a lease or are queued for a lease to queue requests/prompts|TBD|

### Administrator override features

Administrators can take actions that bypass normal operation of the mutex using a special admin API key.

|Name|Description|Target|
|----|-----------|------|
|Kill switch|Disable/enable use of an LLM resource|v1.0|
|Access override|Force lease ownership change for arbitrary duration or until further notice|v1.0|
|Queue tampering|Freely edit queue by adding, removing, or moving the positions of members of the queue|v1.0|

### Security features

Security-related features and improvements.

|Name|Description|Target|
|----|-----------|------|
|TLS/HTTPS support|Service has HTTPS port in addition to HTTP port|TBD|
|Bring your own cert|Allows users to provide their own cert file|TBD|
|Certificate generation|Auto-generates self-signed certificate if none is provided at startup|TBD|

### Observability features

Observability-related features and improvements.

|Name|Description|Target|
|----|-----------|------|
|Prometheus metrics|Metric publication using Prometheus|TBD|

# Appendix

## References

### Ollama API

The [Ollama API spec](https://docs.ollama.com/api/introduction) will be pretty important here as most consumers (including me) will be using it for their LLM provider. Ideally, this API will adhere closely to that same API spec, diverting only as necessary.

If possible, having a mode of use that requires only usage of APIs with identical spec to Ollama would be good for out of the box compatibility with additional optional API fields or APIs for advanced usage.

## Notes to Self

- "Class" of resource - You may have a *n* instances of a model (or a card that can handle multiple concurrent requests, for example) that should be treated identically, instead of listing as separate resources you can combine them into 1 resource with a specified *capacity* for parallel operation.
- Compute resources may be pooled, allowing variable capacity between different models

## AI Use Disclosure

As of right now, no AI has been used on this project.
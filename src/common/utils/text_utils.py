import re

def slugify(input: str) -> str:
    # Check non-empty input
    if not input:
        raise ValueError("Cannot slugify an empty string")

    # First, force lowercasing and replace runs of invalid characters with a hyphen
    slug = re.sub(r"[^a-z0-9-]+", "-", input.lower())
    # Next, combine runs of hyphens into a single hyphen (edge case)
    slug = re.sub(r"[-]{2,}", "-", slug)

    # If length is greater than one, at least one non-hyphen exists at this point, if only one check that its not a hyphen
    if len(slug) == 1 and slug == "-":
        raise ValueError("Cannot slugify a string with no letters or numbers")

    # Finally, remove preceding and trailing hyphens if present
    if slug[0] == "-":
        slug = slug[1:]
    if slug[-1] == "-":
        slug = slug[:-1]

    return slug

def is_valid_slug(input: str) -> bool:
    # Empty string is not a valid slug
    if not input:
        return False
    
    return re.match(r"^(?:[a-z0-9]+-)*[a-z0-9]+$", input)

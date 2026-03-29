def copy_attr(source, target, ignore_props = []):
    # Get attributes
    all_attributes = dir(source)
    properties = []

    for attr in all_attributes:
        should_copy = (
            not callable(getattr(source, attr))
            and not attr.startswith("_")
            and not 'bl_rna' in attr
            and not attr in ignore_props
        )
            
        if should_copy:
            properties.append(attr)
    
    properties.reverse() # To fix a stupid bug
    
    for i in properties:
        if not target == source and not source.is_property_readonly(i):
            newattr = getattr(source, i)
            setattr(target, i, newattr)

def compare_attribute(method, source, input, is_substring_match = False):
    if isinstance(input, str) and is_substring_match:
        return input.lower() in source.name.lower()
    else:
        return getattr(source, method) == input
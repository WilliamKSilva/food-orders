

def validate_object_missing_fields(object: dict, schema: dict[str, any]) -> str | None:
    object_keys = set(object.keys())
    schema_keys = set(schema.keys())

    if object_keys != schema_keys:
        missing_fields = schema_keys.difference(object_keys)

        if len(missing_fields) > 0:
            return f"missing fields {missing_fields}"

    return None 

def validate_object_types(object: dict, schema: dict[str, any], wrong_types: dict) -> dict:
    for k, v in object.items():
        expected_type = schema[k]
        found_type = type(v)

        if found_type == dict:
            found = {}
            for fk, fv in v.items():
                found[fk] = fv 

            err = validate_object_missing_fields(found, expected_type)
            if err != None:
                raise Exception(f"{k}: {err}")

            wrong_types = validate_object_types(found, expected_type, wrong_types)
            continue
            
        if expected_type != found_type:
            wrong_types[k] = {
                "found_type": found_type,
                "expected_type": expected_type
            }

    return wrong_types

def validate_payload(payload: dict, schema: dict[str, any], method:str):
    # Validate missing fields
    errMessage = validate_object_missing_fields(payload, schema)
    # On missing fields throw error right away
    if errMessage != None:
        raise Exception(f"{method} {errMessage}")

    # Validate wrong data types for a valid payload
    errMessage = f"fields have wrong type ["
    wrong_types = validate_object_types(payload, schema, {})

    if len(wrong_types) > 0:
        for i, (k, v) in enumerate(wrong_types.items()):
            found_type = v["found_type"]
            expected_type = v["expected_type"]
            field_name = k
            last_index = i == len(wrong_types) - 1
            errMessage += f"\\{field_name}\\ 'expected': {expected_type} -> 'found': {found_type}"

            if last_index:
                errMessage += "]"
            else:
                errMessage += ", "

        raise Exception(f"{method} {errMessage}")
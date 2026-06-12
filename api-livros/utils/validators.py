def validate_fields(data, required_fields):
    fields_error = []

    for key in required_fields:
        if data.get(key) is None:
            fields_error.append(key)

    if len(fields_error) > 0:
        return  {
                    "message": "Os campos a seguir são obrigatórios",
                    "fields": fields_error
                }, 400

    return {}, 201
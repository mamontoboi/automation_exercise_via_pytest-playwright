PRODUCT_LIST_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "products"],
    "properties": {
        "responseCode": {"type": "integer"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "price", "brand", "category"],
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "price": {"type": "string"},
                    "brand": {"type": "string"},
                    "category": {
                        "type": "object",
                        "required": ["category", "usertype"],
                        "properties": {
                            "category": {"type": "string"},
                            "usertype": {
                                "type": "object",
                                "required": ["usertype"],
                                "properties": {
                                    "usertype": {"type": "string"},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

BRAND_LIST_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "brands"],
    "properties": {
        "responseCode": {"type": "integer"},
        "brands": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "brand"],
                "properties": {
                    "id": {"type": "integer"},
                    "brand": {"type": "string"},
                },
            },
        },
    },
}

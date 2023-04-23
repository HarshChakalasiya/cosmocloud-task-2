from pydantic import BaseModel as PydanticBaseModel

def snake_case_to_camel_case(string: str):
    temp = string.lower().split('_')

    conv_string = temp[0] + ''.join(ele.title() for ele in temp[1:])
    return conv_string[0].lower() + conv_string[1:]

class BaseModel(PydanticBaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        alias_generator = snake_case_to_camel_case
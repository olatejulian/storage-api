from datetime import datetime
from src.utils.app_types import Id
from typing import Union, Optional
from src.utils.pydantic_base_schema import BaseSchema
from src.utils.all_fields_optional import AllFieldsOptional

class FileMetadataSchema(BaseSchema):
    name: str
    path: str
    public: bool
    url_path: str
    user_id: Id
    expire_at: Optional[Union[datetime, None]]
    updated_at: Optional[datetime]
    created_at: Optional[datetime]

class FileMetadataCreate(FileMetadataSchema):
    pass

class FileMetadataUpdate(FileMetadataSchema, metaclass=AllFieldsOptional):
    pass

class FileMetadata(FileMetadataSchema):
    id: Id

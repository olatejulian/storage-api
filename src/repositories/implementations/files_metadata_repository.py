from interface import implements
from src.utils.app_types import Id
from src.repositories.interfaces.files_metadata_interface import IFilesMetadataRepository
from src.schemas.file_metadata_schema import FileMetadataCreate, FileMetadataUpdate, FileMetadata

class FilesMetadataRepository(implements(IFilesMetadataRepository)):
    def __init__(self, files_metadata: FilesMetadataModel = FilesMetadataModel())
    def create(self, file_metadata: FileMetadataCreate) -> Id:
        pass

    def read(self, id: Id) -> FileMetadata:
        pass

    def update(self, id: Id, file_metadata: FileMetadataUpdate) -> None:
        pass

    def delete(self, id: Id) -> None:
        pass
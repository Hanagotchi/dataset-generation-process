from repository.repository import Repository
from scripts.photos import export_log_content, export_log_photos
from scripts.measurements import export_measurements

if __name__ == '__main__':
    repository = Repository()
    export_log_photos(repository, None)
    export_log_content(repository, None)
    export_measurements(repository, None)

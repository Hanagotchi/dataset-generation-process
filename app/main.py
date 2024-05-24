from repository.repository import Repository
from scripts.photos import export_log_photos


if __name__ == '__main__':
    repository = Repository()
    export_log_photos(repository, None)
    #print(repository.get_all_photo_links(None))

from repository.Plants import Repository


if __name__ == '__main__':
    repository = Repository()
    print(repository.get_all_photo_links(None))

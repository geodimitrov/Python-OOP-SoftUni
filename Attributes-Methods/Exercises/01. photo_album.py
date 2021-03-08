class PhotoAlbum:
    MAX_PHOTO_COUNT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)


    def add_photo(self, label):
        for page in self.photos:
            page_index = self.photos.index(page) + 1
            if len(page) < PhotoAlbum.MAX_PHOTO_COUNT:
                page.append(label)
                photo_index = page.index(label) + 1
                return f"{label} photo added successfully on page {page_index} slot {photo_index}"
        return "No more free spots"


    def display(self):
        dash_separator = "-----------"
        result = ""
        for page in self.photos:
            result += f"{dash_separator}\n{' '.join('[]' for photo in page)}\n"
        return f"{result + dash_separator}\n"


# Test Code
album = PhotoAlbum(2)
album2 = PhotoAlbum.from_photos_count(16)
print(album2.pages)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
class PhotoAlbum:
    MAX_PHOTO_COUNT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(pages)]
        self.capacity = len(self.photos) * self.MAX_PHOTO_COUNT

    @staticmethod
    def has_avail_spots(photos, capacity):
        photos_count = sum(len(page) for page in photos)
        return photos_count < capacity

    @staticmethod
    def page_repr(page):
        dash_separator = "-----------"
        return f"{dash_separator}\n{' '.join('[]' for photo in page)}\n"

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def add_photo_to_available_spot(self, label):
        for i in range(len(self.photos)):
            page_index = i + 1
            page = self.photos[i]
            if len(page) < self.MAX_PHOTO_COUNT:
                page.append(label)
                photo_index = page.index(label) + 1
                return f"{label} photo added successfully on page {page_index} slot {photo_index}"

    def add_photo(self, label):
        if not self.has_avail_spots(self.photos, self.capacity):
            return "No more free spots"

        return self.add_photo_to_available_spot(label)

    def display(self):
        return "".join(self.page_repr(page) for page in self.photos) + "-----------\n"


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
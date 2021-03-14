class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return "\n".join(doc.__repr__() for doc in self.documents)

    @staticmethod
    def get_object(object_id, objects):
        return [obj for obj in objects if obj.id == object_id][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_object(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_object(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_object(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove(self.get_object(category_id, self.categories))

    def delete_topic(self, topic_id):
        self.topics.remove(self.get_object(topic_id, self.topics))

    def delete_document(self, document_id):
        self.documents.remove(self.get_object(document_id, self.documents))

    def get_document(self, document_id):
        return self.get_object(document_id, self.documents)
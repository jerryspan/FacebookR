import hashlib


class Post:
    """
    Holder class that contains the data of one (processed) facebook post
    """
    COLL_POST_ID = "_id"
    COLL_USER_ID = "user_id"
    COLL_MESSAGE = "message"
    COLL_DATE = "date"
    COLL_LINK = "link"
    COLL_REACTIONS = "reactions"
    COLL_EMOTION = "emotion"
    COLL_SENTIMENT = "sentiment"
    COLL_COMMENT_EMOTION = "comments_emotion"
    COLL_COMMENT_SENTIMENT = "comments_sentiment"
    COLL_OFF_TOPIC = "off_topic"

    VALID_COLUMNS = [COLL_POST_ID, COLL_USER_ID, COLL_MESSAGE, COLL_DATE, COLL_LINK, COLL_REACTIONS,
                     COLL_COMMENT_SENTIMENT, COLL_COMMENT_EMOTION, COLL_SENTIMENT, COLL_EMOTION, COLL_OFF_TOPIC]
    MANDATORY_COLUMNS = [COLL_POST_ID, COLL_USER_ID, COLL_MESSAGE, COLL_DATE, COLL_LINK, COLL_REACTIONS]

    def __init__(self, structure: dict):
        self.__check_post(structure)
        self.data = structure

    def __check_post(self, post: dict):
        """
        Check that the dictionary can be parsed to a valid post (that it contains all the necessary data and no data that is invalid)
        
        :param post: The dictionary that contains the post's data
        """
        for key, value in post.items():
            assert key in self.VALID_COLUMNS, "Post contains invalid key: '{key}'".format(key=key)
            assert isinstance(value, (
                str, dict, list, bool,
                float)), "Post invalid. The entry for the key '{key}' is invalid: '{value}'".format(
                key=key,
                value=value)

        for key in self.MANDATORY_COLUMNS:
            assert key in post, "Mandatory key missing in post: '{key}'".format(key=key)

    @staticmethod
    def create_from_single_values(post_id: str, user_id: str, message: str, date: str, link: str, reactions: dict,
                                  off_topic: bool):
        """
        Creates a post object from single post values
        
        :param post_id: The id of the post
        :param user_id: The id of the user that created the post
        :param message: The message/content of the post 
        :param date: The date of the post
        :param link: The facebook link of the post
        :param reactions: The facebook user reactions
        :param off_topic: True if this post belongs to an off_topic company (no supermarket)
        :return: A Post object
        """

        data = {Post.COLL_POST_ID: post_id,
                Post.COLL_USER_ID: user_id,
                Post.COLL_MESSAGE: message,
                Post.COLL_DATE: date,
                Post.COLL_LINK: link,
                Post.COLL_REACTIONS: reactions,
                Post.COLL_OFF_TOPIC: off_topic}

        return Post(data)

    @property
    def post_id(self) -> str:
        return self.data[Post.COLL_POST_ID]

    @property
    def user_id(self) -> str:
        return self.data[Post.COLL_USER_ID]

    @property
    def message(self) -> str:
        return self.data[Post.COLL_MESSAGE]

    @property
    def date(self) -> str:
        return self.data[Post.COLL_DATE]

    @property
    def link(self) -> str:
        return self.data[Post.COLL_LINK]

    @property
    def reactions(self) -> dict:
        return self.data[Post.COLL_REACTIONS]

    @property
    def sentiment(self) -> float:
        if Post.COLL_SENTIMENT in self.data:
            return self.data[Post.COLL_SENTIMENT]

    @sentiment.setter
    def sentiment(self, sentiment: float):
        self.data[Post.COLL_SENTIMENT] = sentiment

    @property
    def emotion(self) -> list:
        if Post.COLL_EMOTION in self.data:
            return self.data[Post.COLL_EMOTION]
        else:
            return []

    @emotion.setter
    def emotion(self, emotion: list):
        self.data[Post.COLL_EMOTION] = emotion

    @property
    def comment_sentiment(self) -> float:
        if Post.COLL_COMMENT_SENTIMENT in self.data:
            return self.data[Post.COLL_COMMENT_SENTIMENT]

    @comment_sentiment.setter
    def comment_sentiment(self, comment_sentiment: float):
        self.data[Post.COLL_COMMENT_SENTIMENT] = comment_sentiment

    @property
    def comment_emotion(self) -> list:
        if Post.COLL_COMMENT_EMOTION in self.data:
            return self.data[Post.COLL_COMMENT_EMOTION]
        else:
            return []

    @comment_emotion.setter
    def comment_emotion(self, comment_emotion: list):
        self.data[Post.COLL_COMMENT_EMOTION] = comment_emotion

    @property
    def off_topic(self) -> bool:
        return self.data[Post.COLL_OFF_TOPIC] if Post.COLL_OFF_TOPIC in self.data else False

    @off_topic.setter
    def off_topic(self, off_topic: bool):
        self.data[Post.COLL_OFF_TOPIC] = off_topic


class Comment:
    """
    Holder class that contains the data of one (processed) facebook post
    """
    COLL_ID = "_id"
    COLL_PARENT_ID = "parent_id"
    COLL_USER_ID = "user_id"
    COLL_CONT = "content"
    COLL_DATE = "date"

    VALID_COLUMNS = [COLL_ID, COLL_PARENT_ID, COLL_USER_ID, COLL_CONT, COLL_DATE]
    MANDATORY_COLUMNS = [COLL_ID, COLL_PARENT_ID, COLL_USER_ID, COLL_CONT, COLL_DATE]

    def __init__(self, structure: dict):
        self.__check_comment(structure)
        self.data = structure

    def __check_comment(self, comment: dict):
        """
        Check that the dictionary can be parsed to a valid comment (that it contains all the necessary data and no data that is invalid)
        
        :param comment: The dictionary that contains the comment's data
        """
        for key, value in comment.items():
            assert key in self.VALID_COLUMNS, "Comment contains invalid key: '{key}'".format(key=key)
            assert isinstance(value,
                              str), "Comment invalid. The entry for the key '{key}' is invalid: '{value}'".format(
                key=key,
                value=value)

        for key in self.MANDATORY_COLUMNS:
            assert key in comment, "Mandatory key missing in comment: '{key}'".format(key=key)

    @staticmethod
    def create_from_single_values(comment_id: str, parent_id: str, user_id: str, content: str, date: str):
        """
        Creates a comment object from single comment values
        
        :param comment_id: The id of the comment
        :param parent_id: The id of the parent-comment (if there is no parent the id is -1)
        :param user_id: The id of the user that created this comment
        :param content: The content of the comment
        :param date: The date of the comment
        :return: A Comment object
        """

        data = {Comment.COLL_ID: comment_id,
                Comment.COLL_PARENT_ID: parent_id,
                Comment.COLL_USER_ID: user_id,
                Comment.COLL_CONT: content,
                Comment.COLL_DATE: date}

        return Comment(data)

    @property
    def id(self) -> str:
        return self.data[Comment.COLL_ID]

    @property
    def parent_id(self) -> str:
        return self.data[Comment.COLL_PARENT_ID]

    @property
    def content(self) -> str:
        return self.data[Comment.COLL_CONT]

    @property
    def date(self) -> str:
        return self.data[Comment.COLL_DATE]


class Emotion:
    """
    Holder class that contains the data of one emotion for a word
    """
    COLL_ID = "_id"
    COLL_EMOTION = "emotion"

    EMOTION_TYPES = ["ANGER", "ANTICIPATION", "DISGUST", "FEAR", "JOY", "SADNESS", "SURPRISE", "TRUST"]

    VALID_COLUMNS = [COLL_ID, COLL_EMOTION]
    MANDATORY_COLUMNS = [COLL_ID, COLL_EMOTION]

    def __init__(self, structure: dict):
        self.__check_emotion(structure)
        self.data = structure

    def __check_emotion(self, emotion: dict):
        """
        Check that the dictionary can be parsed to a valid emotion (that it contains all the necessary data and no data that is invalid)

        :param emotion: The dictionary that contains the emotion's data
        """
        for key, value in emotion.items():
            assert key in self.VALID_COLUMNS, "Emotion contains invalid key: '{key}'".format(key=key)
            assert isinstance(value,
                              (
                                  str, float,
                                  list)), "Emotion invalid. The entry for the key '{key}' is invalid: '{value}'" \
                .format(key=key, value=value)

        for key in self.MANDATORY_COLUMNS:
            assert key in emotion, "Mandatory key missing in emotion: '{key}'".format(key=key)

    @staticmethod
    def create_from_single_values(emotion_name: str, emotion: list):
        """
        Creates a emotion object from single emotion values

        :param emotion_name: The original name that was searched
        :param emotion: The emotion list
        :return: An emotion object
        """

        data = {Emotion.COLL_ID: emotion_name,
                Emotion.COLL_EMOTION: emotion}

        return Emotion(data)

    @property
    def id(self) -> str:
        return self.data[Emotion.COLL_ID]

    # [anger, anticipation, disgust, fear, joy, sadness, surprise, trust]
    @property
    def emotion(self) -> list:
        return self.data[Emotion.COLL_EMOTION]


class Sentence:
    """
    Holder class that contains the data of one sentence for a word
    """
    COLL_ID = "_id"
    COLL_CONTENT = "content"
    COLL_EMOTION = "emotion"
    COLL_PREDICTED = "predicted"

    VALID_COLUMNS = [COLL_ID, COLL_CONTENT, COLL_EMOTION, COLL_PREDICTED]
    MANDATORY_COLUMNS = [COLL_ID, COLL_CONTENT, COLL_EMOTION]

    def __init__(self, structure: dict):
        self.__check_sentence(structure)
        self.data = structure

    def __check_sentence(self, sentence: dict):
        """
        Check that the dictionary can be parsed to a valid sentence (that it contains all the necessary data and no data that is invalid)

        :param sentence: The dictionary that contains the sentence's data
        """
        for key, value in sentence.items():
            assert key in self.VALID_COLUMNS, "Sentence contains invalid key: '{key}'".format(key=key)
            assert isinstance(value,
                              (
                              str, list, bool)), "Sentence invalid. The entry for the key '{key}' is invalid: '{value}'" \
                .format(key=key, value=value)

        for key in self.MANDATORY_COLUMNS:
            assert key in sentence, "Mandatory key missing in sentence: '{key}'".format(key=key)

    @staticmethod
    def create_from_single_values(sentence: str, emotions: list, predicted: bool):
        """
        Creates a sentence object from single sentence values

        :param sentence: The sentence's content
        :param emotions: The emotions list
        :return: A sentence object
        """

        data = {Sentence.COLL_ID: hashlib.md5(sentence.encode('utf-8')).hexdigest(),
                Sentence.COLL_CONTENT: sentence,
                Sentence.COLL_EMOTION: emotions,
                Sentence.COLL_PREDICTED: predicted}

        return Sentence(data)

    @property
    def id(self) -> str:
        return self.data[Sentence.COLL_ID]

    @property
    def emotion(self) -> list:
        return self.data[Sentence.COLL_EMOTION]

    @property
    def content(self) -> str:
        return self.data[Sentence.COLL_CONTENT]

    @property
    def predicted(self) -> bool:
        return self.data[Sentence.COLL_PREDICTED] if Sentence.COLL_PREDICTED in self.data else False

    @predicted.setter
    def predicted(self, predicted: bool):
        self.data[Sentence.COLL_PREDICTED] = predicted

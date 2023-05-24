import dataclasses


@dataclasses.dataclass
class Paper:
    paper_id: str
    title: str
    abstract: str

    @classmethod
    def from_json(cls, json):
        return cls(
            paper_id=json['paperId'],
            title=json['title'],
            abstract=json['abstract']
        )


@dataclasses.dataclass
class SearchOutput:
    total_hits: int
    offset: int
    next_: int
    data: list[Paper]

    @classmethod
    def from_json(cls, json):
        return cls(
            total_hits=json['total'],
            offset=json['offset'],
            next_=json['next'],
            data=[Paper.from_json(d) for d in json['data']]
        )

import dataclasses


@dataclasses.dataclass
class PageList:
    pages: list[str]

    def get_middle_element(self) -> str:
        assert len(self.pages) % 2 == 1
        middle = (len(self.pages) - 1) // 2
        return self.pages[middle]


@dataclasses.dataclass
class Rule:
    a: str
    b: str

    def is_applicable(self, pages: PageList) -> bool:
        return self.a in pages.pages and self.b in pages.pages

    def is_valid(self, pages: PageList) -> bool:
        index_a = pages.pages.index(self.a)
        index_b = pages.pages.index(self.b)
        return index_a < index_b

    @staticmethod
    def is_all_rules_applicable_and_correct(rules: list['Rule'], pages: PageList) -> bool:
        res = True
        for r in rules:
            if not r.is_applicable(pages):
                continue
            if not r.is_valid(pages):
                res = False
                break

        return res


def main():
    rules: list[Rule] = []
    pagelists: list[PageList] = []
    with open('indput1.txt') as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                rules.append(Rule(*line.split('|')))
            if ',' in line:
                pagelists.append(PageList(line.split(',')))

    acc = 0
    for pagelist in pagelists:
        if Rule.is_all_rules_applicable_and_correct(rules, pagelist):
            print(f'{pagelist} is correct with {pagelist.get_middle_element()} in the middle')
            acc += int(pagelist.get_middle_element())

    print(f'result: {acc}')


if __name__ == '__main__':
    main()

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

    @staticmethod
    def get_ordered_page_set(rules: list['Rule']) -> list[str]:
        page_set = set()
        for rule in rules:
            page_set.add(rule.a)
            page_set.add(rule.b)

        list_of_pages = list(page_set)
        while True:
            did_swap = False
            for a in range(0, len(list_of_pages)):
                for b in range(a+1, len(list_of_pages)):
                    if a == b:
                        continue
                    pseudo_list = PageList([list_of_pages[a], list_of_pages[b]])
                    for rule in rules:
                        if rule.is_applicable(pseudo_list) and not rule.is_valid(pseudo_list):
                            val_a = list_of_pages[a]
                            val_b = list_of_pages[b]
                            list_of_pages[a] = val_b
                            list_of_pages[b] = val_a
                            did_swap = True
                            print(f'swapped {val_a} in {a} and {val_b} in {b} by the rule {rule}')
                            break
                if did_swap:
                    break
            if not did_swap:
                break
        return list_of_pages

    @staticmethod
    def fix_pages_order(ordered_pages: list[str], pages: PageList) -> PageList | None:
        fixed_sequence = []
        print(ordered_pages)
        for page in ordered_pages:
            if page in pages.pages:
                fixed_sequence.append(page)
        return PageList(fixed_sequence)


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
        applicable_rules = []
        for rule in rules:
            if rule.is_applicable(pagelist):
                applicable_rules.append(rule)
        ordered_pages = Rule.get_ordered_page_set(applicable_rules)

        if not Rule.is_all_rules_applicable_and_correct(rules, pagelist):
            fixed = Rule.fix_pages_order(ordered_pages, pagelist)
            print(f'{pagelist} -> {fixed}')
            acc += int(fixed.get_middle_element())
    print(f'result: {acc}')


if __name__ == '__main__':
    main()

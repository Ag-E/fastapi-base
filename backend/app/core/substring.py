class SubStringService:
    @staticmethod
    def find_longest_str_len(input_string: str) -> int:
        biggest_sub_str = ""
        candidate_sub_str = ""
        for i in range(len(input_string)):
            if input_string[i] not in candidate_sub_str:
                candidate_sub_str += input_string[i]
                if i == len(input_string) - 1:
                    biggest_sub_str = SubStringService.replace_biggest_sub_str(
                        biggest_sub_str, candidate_sub_str
                    )
            else:
                biggest_sub_str = SubStringService.replace_biggest_sub_str(
                    biggest_sub_str, candidate_sub_str
                )
                found_position = candidate_sub_str.find(input_string[i]) + 1
                candidate_sub_str = (
                    candidate_sub_str[found_position:] + input_string[i]
                )
        return len(biggest_sub_str)

    @staticmethod
    def replace_biggest_sub_str(
        biggest_sub_str: str, candidate_sub_str: str
    ) -> str:
        if len(candidate_sub_str) > len(biggest_sub_str):
            return candidate_sub_str
        else:
            return biggest_sub_str


if __name__ == "__main__":
    res = SubStringService.find_longest_str_len("pwwkewrtyryr")
    print(res)

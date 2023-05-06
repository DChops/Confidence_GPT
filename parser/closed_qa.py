class parser:
    def parse(self, ans_list:list)-> dict:
        ans_dict = {}
        for i in ans_list:
            index = i.find("The answer is ")
            if(index==-1):
                continue

            index += 14
            ans = i[index:-1]
            if(ans in ans_dict):
                ans_dict[ans] += 1
            else:
                ans_dict[ans] = 1
        return ans_dict
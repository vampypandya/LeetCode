class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        return_list = []
        for item in items:
            ids = item[0]
            val = item[1]
            if (ids not in dic):
                dic[ids] = [val]
            else:
                if (len(dic[ids]) < 5):
                    temp_list = dic[ids]
                    temp_list.append(val)
                    dic[ids] = temp_list
                else:
                    if (val > min(dic[ids])):
                        temp_list = dic[ids]
                        mini = min(temp_list)
                        temp_list.remove(mini)
                        temp_list.append(val)
                        dic[ids] = temp_list

        for key in dic.keys():
            return_list.append([key, (sum(dic[key]) / 5)])
        return return_list

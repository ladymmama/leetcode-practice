"""
本题是想让我们找出最长的重复字符的字符串的长度，换句话说
我们其实就是找满足以下条件的最大sub-string的长度就可以了：
条件为：(子字符串长度-出现次数最多的字符串的个数) <= k
备注：这里我们介绍一个库的用法，defaultdict
当我使用普通的字典时，用法一般是dict={},添加元素的只需要dict[element] =value即，
调用的时候也是如此，dict[element] = xxx,但前提是element字典里，如果不在字典里就会报错
这时defaultdict就能排上用场了，defaultdict的作用是在于，
当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，而下面我们用int，对应的默认值为0
"""

from collections import defaultdict
class Solution_1:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = defaultdict(int) # 记录窗口内每个字符出现过的次数
        res, left, right= 0, 0, 0 #left记录滑动窗口左边界，right记录右边界,res返回结果，全部初始化为0
        count_s = len(s) #字符串的长度，也就是一共有多少个字符
        max_repeat_count = 0 # 窗口内出现最多次字符的次数

        #这里开始遍历字符串，以右边界和字符串长度为界
        while right < count_s:
            #我们需要累加出现字符的个数，然后更新出现最多字符的个数
            window_count[s[right]] += 1 # 次数加一
            # 由于窗口只有 s[right] 增加了一次，那么出现最多次字符的次数 只需要和这个字符的字符比较就可以了
            max_repeat_count = max(max_repeat_count, window_count[s[right]]) # 更新出现最多次字符的次数

            #更新以后我们就可以判断当前的滑动窗口是否满足之前说的那个条件了
            #如果不满足，去掉的字符要在window_count里面减一，然后left就向右移动一步，直到满足条件
            while right - left + 1 - max_repeat_count > k: # left 向边移动
                window_count[s[left]] -= 1 
                #max_repeat_count = max(max_repeat_count, window_count[s[left]])
                left += 1

            #不大于k的情况
            res = max(res,right-left+1) # 窗口内的单词个数
            right += 1
        return res

"""
解法2思路是同样的，唯一的不同在于上述解法我们用了defaultdict来记录每个字符的出现次数
本题我们直接构造一个含有26个字母的列表，
然后用ord函数返回对应的ASCII或者Unicode值来进行类似字典的一个key对一个value的操作
其余部分全部同理
"""
class Solution_2:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = res = 0
        max_repeat_count = 0
        window_count=[0]*26 #构造涵盖所有26个字母的列表
        while right<len(s):
            #这里就是转换为unicode值，之所以减65是因为大写A对应十进制整数就是65
            #所以相当于65-65我们从0开始网上增加出现次数，与上个解法同理
            window_count[ord(s[right])-65]+=1
            max_repeat_count=max(max_repeat_count,max(window_count))
            while (right-left+1-max_repeat_count)>k:
                  #这里同样，之前用字典表达的地方全部都需要转换
                  window_count[ord(s[left])-65] -= 1
                  #max_repeat_count = max(max_repeat_count, window_count[ord(s[left])-65])
                  left += 1
            res=max(res,right-left+1)
            right += 1
        return res

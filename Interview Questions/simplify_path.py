'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

Input: "/a/./b/../../c/"
Output: "/c"

Input: "/a/./b/../../c/"
Output: "/c"

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        frags  = path.split("/")
        for frag in frags:
            if frag in ["", "."]:
                continue
            elif frag == "..": 
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(frag)
        return "/" + "/".join(stack)

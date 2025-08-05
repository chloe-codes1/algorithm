class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []

        for part in parts:
            if not part or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        if not stack:
            return '/'

        return '/' + '/'.join(stack)

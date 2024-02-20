class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                top_1 = st.pop()
                top_2 = st.pop()
                if token == '+':
                    st.append(top_2 + top_1)
                elif token == '-':
                    st.append(top_2 - top_1)
                elif token == '*':
                    st.append(top_2 * top_1)
                else:
                    st.append(int(top_2/top_1))
            else:
                st.append(int(token))
        return st.pop()
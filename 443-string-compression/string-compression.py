class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Count the number of same characters
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


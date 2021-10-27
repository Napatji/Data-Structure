class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
    def checkParen(self,Parenthesis): ###เช็กวงเล็บ
        open_paren = ["[","{","("] ###ลิสต์ที่ใช้ตรวจสอบวงเล็บเปิด
        close_paren = ["]","}",")"] ###ลิสต์ที่ใช้ตรวจสอบวงเล็บปิด
        checking = [] ###เก็บวงเล็บเปิดจากข้อความ
        close_left = [] ###เก็บวงเล็บปิดจากข้อความ
        check_open = [] ###เช็กจำนวนวงเล็บเปิด
        check_close = [] ###เช็กจำนวนวงเล็บปิด
        check_letter = [] ###เช็กตัวอักษร
        for ele in Parenthesis: ###ลูปแทน element ทุกตัวในประโยคที่พิมพ์ 
            if ele in open_paren: ###เจอวงเล็บเปิด
                checking.append(ele) ###นำเข้าไปรอตรวจ
                check_open.append(ele) ###นำเข้าไปนับจำนวน
            elif ele in close_paren: ###เจอวงเล็บปิด
                check_close.append(ele) ###นำเข้าไปรอนับจำนวน
                ref = close_paren.index(ele) ###หาอินเด็กซ์ของชนิดวงเล็บที่เจอในลิสต์ตรวจสอบ
                if (len(checking) > 0) and (open_paren[ref] == checking[len(checking) - 1]): ###เช็กว่าวงเล็บที่เจอเป็นชนิดเดียวกันมั้ย
                    checking.pop()
                elif (len(checking) > 0) and (open_paren[ref] != checking[len(checking) - 1]): ###ถ้าไม่ตรงจะ Unmatched
                    return "Unmatch open-close"
                else:
                    close_left.append(ele)
            elif ele not in check_open and ele not in check_close: ###กรณีเจอตัวอักษร
                check_letter.append(ele)       

        if len(checking) == 0 and len(check_open) == len(check_close):###วงเล็บไม่ขาดไม่เกิน
            return "MATCH"
        elif len(checking) == 0 and len(check_close) > 0:###วงเล็บปิดเกิน
            if len(check_open) == 0 and len(check_letter) == 0:###ใส่มาแต่วงเล็บปิด
                return ("close paren excess")   #{} : {}".format(len(check_close),str(Parenthesis)))
            elif len(check_letter) > 0 and check_close > check_open:###มีตัวอักษร
                diff = len(check_close)-len(check_open)
                return ("close paren excess   {} : {}".format(diff,''.join(word[0] for word in close_left)))
            else:###วงเล็บปิดเหลือ
                return "close paren excess"
        elif len(checking) > 0:###วงเล็บเปิดเหลือ
            if len(check_close) == 0 and len(check_letter) == 0:###ใส่มาแต่วงเล็บเปิด
                return ("open paren excess   {} : {}".format(len(check_open),str(Parenthesis)))
            elif len(check_letter) > 0:###มีตัวอักษร
                return ("open paren excess   {} : {}".format(len(checking),''.join(word[0] for word in checking)))
            else:###เหลือวงเล็บเปิด
                return ("open paren excess")
        else:###ใส่วงเล็บเปิด-ปิดคนละชนิดกัน
            return "Unmatch open-close"
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    parenthesis = input("Enter expresion : ")
    print(parenthesis, stack.checkParen(parenthesis))
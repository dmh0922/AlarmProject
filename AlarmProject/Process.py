import INFO

class Process :

    def Exp_Coupon(text) :

        try:
            Coupons = text.split(',')

            for Data in Coupons :
                name, cycle, left = Data.split()

                name = f'{name} ({cycle})'
                cycle = INFO.cast_Num(cycle) * INFO.MIN
                left = INFO.cast_Num(left)

                INFO.info_Coupon = [name,cycle,left]

            return True
        except:
            return False

    def Exp_Bonus(text) :

        if text in ['ㄴ','ㄴㄴ','s','ss'] :
            INFO.info_Bonus = ["등록된 정보가 없습니다."]
            return True

        try:
            place, when, left = text.split(',')
            when = INFO.cast_Num(when)
            left = INFO.cast_Num(left)
            INFO.info_Bonus = [place,when,left]

            return True
        except:
            return False
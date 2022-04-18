import INFO

class Notice :

    def Ready() :
        embed = INFO.discord.Embed(title="준비 완료!" ,color=0x00ff56)

        embed.add_field(name="총 시간 : ", value=f"{str( INFO.work_time // INFO.MIN ) + '분'}", inline=False)
        embed.add_field(name="사용할 쿠폰 : ", value=f"{INFO.info_Coupon}", inline=False)
        embed.add_field(name="받을 보너스 : ", value=f"{INFO.info_Bonus[0]}", inline=False)

        embed.set_footer(text="시작은 \n!!r ㄱㄱ , !!r rr , !!r 시작 \n중 입력해 주세요.\n취소는 !!취소 , !!cnlth 입니다.")
        return embed

    def Exp_Coupon(time_passed, Coupon_name, Coupon_left):
        return INFO.discord.Embed(title=f"경과 시간 : {time_passed}\n{Coupon_name}을(를) 사용해주세요.\n남은 {Coupon_name}은(는) {Coupon_left}개 입니다." ,color=0x0054FF)

    def Exp_Bonus(where,num):
        return INFO.discord.Embed(title=f"1분 전입니다.\n위치 : {where}\n남은 수령 횟수 : {num}번",color=0x5F00FF)
    
    def End() :
        return INFO.discord.Embed(title="끝!",color=0x62c1cc)
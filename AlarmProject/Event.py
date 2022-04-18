import INFO

class Event :

    @INFO.client.event
    async def on_message(message) :
        print("Connected!")
        await INFO.client.change_presence(status = INFO.discord.Status.online, activity=None)
        return
    
    @INFO.client.event
    async def on_message(message) :
        msg = message.content
        if (message.author == INFO.client.user) : return

        if msg in ['!!취소', '!!cnlth'] :
            INFO.state = "On"
            await message.reply("정상적으로 취소됐어요.")

        if (INFO.state == "gotTime") :

            INFO.info_Coupon = msg

            if msg in ['ㄴ','ㄴㄴ','s','ss'] :
                INFO.info_Coupon = "등록된 정보가 없습니다."
            elif INFO.Process.Exp_Coupon(msg) :
                pass

            INFO.state = 'gotExpCoupons'
            await message.reply("추가로 받을 보너스 : ")
        
        elif (INFO.state == 'gotExpCoupons') :
            if INFO.Process.Exp_Bonus(msg) :
                INFO.state = 'gotExpBonus'
                await message.reply("정보를 종합중입니다...")
                await INFO.asyncio.sleep(1)
                await message.channel.send(embed=INFO.Notice.Ready())
        
        await INFO.client.process_commands(message)
        return
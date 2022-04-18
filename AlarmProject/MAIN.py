import INFO

@INFO.client.command(aliases = ['r' , 'ㄱ'])
async def main(ctx,*,text) :

    global alarm

    if (INFO.state == 'ON') :

        INFO.work_time = INFO.cast_Num(text)
        unit = INFO.cast_Letter(text)

        if unit in ['초', 'ch']:
            text = str(work_time) + '초'
        elif unit in ['분', 'qns']:
            text = str(work_time) + '분'
            work_time *= 60
        elif unit in ['시간', 'tlrks', 'h', 'hour']:
            text = str(work_time) + '시간'
            work_time *= 60 * 60
        else:
            input_error(ctx)
        
        INFO.state = 'gotTime'
        await ctx.reply(f'{text}동안 사용하실 쿠폰들을 입력해 주세요!')
    
    elif ( text in ['ㄱㄱ', 'rr'] and INFO.state == 'gotExpBonus') :

        INFO.time_now = INFO.time.time()
        INFO.state = 'isRunning'

        await ctx.reply("시작! 알람을 준비합니다.")
        alarms_waiting = [INFO.Alarm.End(ctx)]

        if ( INFO.info_Coupon == "등록된 정보가 없습니다." ) : pass
        else :
            for Coupon in INFO.info_Coupon :
                alarms_waiting.append( INFO.Alarm.Exp_Coupon(ctx,Coupon) )
        
        if ( INFO.info_Bonus == ["등록된 정보가 없습니다."] ) : pass
        else :
            alarms_waiting.append( INFO.Alarm.Exp_Bonus(ctx, INFO.info_Bonus, INFO.time_now) )
        
        alarm = INFO.asyncio.wait(alarms_waiting)
        await alarm
        INFO.state = 'ON'

@main.error
async def input_error(ctx, error):
  if (INFO.state == 'ON') :
    await ctx.send(INFO.MSG_READY_ERROR)
  else:
    await ctx.send(INFO.MSG_ERROR)

@INFO.client.command(aliases = ['취소' , 'cnlth'])
async def ignore(ctx):
    pass

INFO.client.run(INFO.TOKEN)
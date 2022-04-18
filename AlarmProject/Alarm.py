import INFO

class Alarm :

    async def Exp_Coupon(ctx,info) :
        if (info == "등록된 정보가 없습니다.") : return

        name, cycle, left = info
        time_passed = 0

        while (left > 0) :

            left -= 1
            await INFO.asyncio.sleep(cycle)
            time_passed += cycle // 60

            notice = INFO.Notice.Exp_Coupon(time_passed, name, left)
            await ctx.channel.send(embed=notice)
        
        return

    async def Exp_Bonus(ctx,info,time_now) :
        if (info == "등록된 정보가 없습니다.") : return

        place, when, left = info
        ready_time = when - 1

        left -= 1
        await INFO.asyncio.sleep( INFO.Next_Exp_Bonus(time_now,ready_time) )
        notice = INFO.Notice.Exp_Bonus(place,left)
        await ctx.channel.send(embed=notice)

        while ( left > 0 ) :
            left -= 1
            await INFO.asyncio.sleep(INFO.HOUR)

            notice = INFO.Notice.Exp_Bonus(place,left)
            await ctx.channel.send(embed=notice)
        
        return

    async def End(ctx) :
        await INFO.asyncio.sleep(INFO.work_time)
        await ctx.channel.send(embed=INFO.Notice.End())
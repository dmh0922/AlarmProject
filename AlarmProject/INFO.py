import discord, asyncio, time
from discord.ext import commands

class INFO :
    TOKEN = 'ODgyNjMxMTI3MTYzMDc2NjY4.YS-MSw.JtfEYml3eJlpY40kb2Qw69_qouE'
    client = commands.Bot(command_prefix='!!')
    state = "On"

    MSG_READY_ERROR = "잘못된 형식입니다. '!!취소' 또는 '!!cnlth' 명령으로 준비를 취소할 수 있어요."
    MSG_ERROR = "알 수 없는 말이에요."

    HOUR = 1800
    MIN = 60

    time_now = -1
    work_time = -1

    info_Bonus = []
    info_Coupon = []

    def Next_Exp_Bonus(current_time, expBonus_ready) :
        
        current_min = int(time.strftime('%M', time.localtime(current_time)))
        current_sec = int(time.strftime('%S', time.localtime(current_time)))

        ret = ( expBonus_ready - current_min - 1 )*INFO.MIN + (INFO.MIN - current_sec)
        if (ret < 0) :
            ret += INFO.HOUR
        elif (ret > INFO.HOUR):
            ret -= INFO.HOUR
        
        return ret

    def cast_Num(text) :
        filt = list( filter(str.isdigit, text) )
        return int("".join(filt))
    
    def cast_Letter(text) :
        filt = list( filter(str.isalpha, text) )
        return "".join(filt)

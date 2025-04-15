score = int(input("請輸入成績："))    # 輸入成績再轉成整數並指定給score
if score >=0 and score <= 100:        # 判斷score是否介於0~100之間
    if score >= 100 :
        show = "他媽開掛我要檢舉你"              # score介於100~90時，show指定 "優等"
    elif score >= 90 :
        show = "是人才啊"              # score介於100~90時，show指定 "優等"
    elif score >= 80 :
        show = "是讀書的料"             # score介於89~80時，show指定 "甲等"
    elif score >= 70 :
        show = "加油還有進步空間"             # score介於79~70時，show指定 "乙等"
    elif score >= 60 :
        show = "雖然合格但小心"             # score介於69~60時，show指定 "丙等"
    else :
        show = "需要Rikki的蛤"           # score介於59~0時，show指定 "不及格" 
else:
    show = "應介於0~100之間"  
print("你", show)
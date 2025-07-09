import matplotlib.pyplot as plt
from tabulate import tabulate


# حسين موقري

def graphSPN(job_count, future_at, future_cbt, at_order, cbt_order, job_order, start_time):
    fig, ax_gnt = plt.subplots()
    ax_gnt.set_ylim(0, 5 + (job_count * 15))
    m = max(start_time)
    ax_gnt.set_xlim(0, m + max(cbt_order) + 1)

    job_list = []
    for x in range(job_count):
        job_list.append(15 * (x + 1) - 5)

    ax_gnt.set_yticks(job_list)

    job_name = []
    for x in range(job_count):
        job_name.append("job_" + str(x + 1))
    ax_gnt.set_yticklabels(job_name)

    ax_gnt.grid(True)
    color = ['xkcd:sky blue', 'tab:orange', 'tab:brown', 'tab:gray', 'tab:blue', 'tab:olive', 'tab:pink', 'tab:cyan',
             'tab:purple', 'xkcd:gold', 'xkcd:purple', 'xkcd:lime', 'xkcd:palegreen']

    new_start = []
    new_cbt = []
    for x in range(job_count):
        new_start.append(-1)
        new_cbt.append(-1)
    for x in range(job_count):
        n = job_order[x]
        new_start[n] = start_time[x]
        new_cbt[n] = cbt_order[x]

    enter_point = []
    for x in range(job_count):
        enter_point.append(future_at[x])
    height_point = []
    for x in range(job_count):
        height_point.append(15 * (x + 1) - 5)
    test_list = []
    for x in range(job_count):
        extention = [new_start[x], new_cbt[x]]
        test_list.extend([extention])

    works = []
    plt.plot(enter_point, height_point, 'ro')

    for x in range(job_count):
        works.append([ax_gnt.broken_barh([(test_list[x][0], test_list[x][1])], (((x + 1) * 15) - 10, 10),
                                         facecolors={color[x]})])

    for x in range(job_count):
        works[x]

    annot = ax_gnt.annotate("", xy=(0, 0), xytext=(20, 30), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="yellow", ec="b", lw=2),
                            arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(brokenbar_collection, coll_id, ind, x, y):
        annot.xy = (x, y)
        box = brokenbar_collection.get_paths()[ind].get_extents()
        text = f"{ax_gnt.get_yticklabels()[coll_id].get_text()} index:{ind} duration:{box.x1 - box.x0:.0f} "
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.9)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax_gnt:
            for coll_id, brokenbar_collection in enumerate(ax_gnt.collections):
                cont, ind = brokenbar_collection.contains(event)
                if cont:
                    update_annot(brokenbar_collection, coll_id, ind['ind'][0], event.xdata, event.ydata)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()


def graphHRRN(job_count, final_at, final_cbt, final_job_count, final_current_time_list):
    fig, ax_gnt = plt.subplots()
    ax_gnt.set_ylim(0, 5 + (job_count * 15))
    m = max(final_at)
    qqq = len(final_at)
    ax_gnt.set_xlim(0, m + max(final_current_time_list) + final_cbt[qqq - 1] + 2)

    job_list = []
    for x in range(job_count):
        job_list.append(15 * (x + 1) - 5)

    ax_gnt.set_yticks(job_list)

    job_name = []
    for x in range(job_count):
        job_name.append("job_" + str(x + 1))
    ax_gnt.set_yticklabels(job_name)

    ax_gnt.grid(True)
    color = ['xkcd:sky blue', 'tab:orange', 'tab:brown', 'tab:gray', 'tab:blue', 'tab:olive', 'tab:pink', 'tab:cyan',
             'tab:purple', 'xkcd:gold', 'xkcd:purple', 'xkcd:lime', 'xkcd:palegreen']

    enter_point = []
    for x in range(job_count):
        f = final_job_count.index(x)
        enter_point.append(final_at[f])
    height_point = []
    for x in range(job_count):
        height_point.append(15 * (x + 1) - 5)
    test_list = []
    finding = 0
    for x in range(job_count):
        s = final_job_count.index(finding)
        finding = finding + 1
        extention = final_current_time_list[s], final_cbt[s]
        test_list.extend([extention])

    works = []
    plt.plot(enter_point, height_point, 'ro')

    for x in range(job_count):
        works.append([ax_gnt.broken_barh([(test_list[x][0], test_list[x][1])], (((x + 1) * 15) - 10, 10),
                                         facecolors={color[x]})])

    for x in range(job_count):
        works[x]

    annot = ax_gnt.annotate("", xy=(0, 0), xytext=(20, 30), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="yellow", ec="b", lw=2),
                            arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(brokenbar_collection, coll_id, ind, x, y):
        annot.xy = (x, y)
        box = brokenbar_collection.get_paths()[ind].get_extents()
        text = f"{ax_gnt.get_yticklabels()[coll_id].get_text()} index:{ind} duration:{box.x1 - box.x0:.0f} "
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.9)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax_gnt:
            for coll_id, brokenbar_collection in enumerate(ax_gnt.collections):
                cont, ind = brokenbar_collection.contains(event)
                if cont:
                    update_annot(brokenbar_collection, coll_id, ind['ind'][0], event.xdata, event.ydata)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()


def graphRR(job_count, final_at, final_cbt, final_job_number, fina1_current_time, QT):
    fig, ax_gnt = plt.subplots()
    ax_gnt.set_ylim(0, 5 + (job_count * 15))
    m = max(final_at)
    # ax_gnt.set_xlim(0, m+max(fina1_current_time)+QT+2)
    ax_gnt.set_xlim(0, max(fina1_current_time) + QT + 2)

    job_list = []
    for x in range(job_count):
        job_list.append(15 * (x + 1) - 5)

    ax_gnt.set_yticks(job_list)

    job_name = []
    for x in range(job_count):
        job_name.append("job_" + str(x + 1))
    ax_gnt.set_yticklabels(job_name)

    ax_gnt.grid(True)
    color = ['xkcd:sky blue', 'tab:orange', 'tab:brown', 'tab:gray', 'tab:blue', 'tab:olive', 'tab:pink', 'tab:cyan',
             'tab:purple', 'xkcd:gold', 'xkcd:purple', 'xkcd:lime', 'xkcd:palegreen']

    enter_point = []
    for x in range(job_count):
        f = final_job_number.index(x)
        enter_point.append(final_at[f])
    height_point = []
    for x in range(job_count):
        height_point.append(15 * (x + 1) - 5)
    test_list = []
    '''
        test_list = [[(5, 9), (14, 1), (15, 4), (19, 9), (28, 4), (34, 4), (38, 5)],[(14, 8), (22, 4), (29, 7), (36, 3), (39, 15)],
                 [(5, 5), (14, 1), (15, 4), (19, 9), (28, 4), (34, 4), (38, 5)],[(5, 5), (14, 1), (15, 4), (19, 9), (28, 4), (34, 4), (38, 5)]
                 ]
                 '''
    checklist = []
    for x in range(job_count):
        templist = []
        for y in range(len(final_at)):
            if final_job_number[y] == x:
                e = fina1_current_time[y]
                r = final_cbt[y]
                templist.append((e, r))
        checklist.append(templist)

    for x in range(len(final_at)):
        extention = fina1_current_time[x], final_cbt[x]
        test_list.extend([extention])
    # print(checklist)

    works = []
    plt.plot(enter_point, height_point, 'ro')

    for x in range(job_count):
        works.append([ax_gnt.broken_barh((checklist[x]), (((x + 1) * 15) - 10, 10),
                                         facecolors={color[x]})])

    # works.append(ax_gnt.broken_barh([(8,6)], (20, 10),
    # facecolors={blue}))
    # works=[    ax_gnt.broken_barh([(test_list[0][0],test_list[0][1])], (5, 10),
    #                  facecolors={olive}),    ax_gnt.broken_barh([(8,6)], (20, 10),
    #                 facecolors={blue}),    ax_gnt.broken_barh([(17,7)], (35, 10),
    #                facecolors={pink}),
    #
    #              plt.plot(enter_point, height_point, 'ro')
    #             ]
    for x in range(job_count):
        # works[x] was works[job_count]
        works[x]

    annot = ax_gnt.annotate("", xy=(0, 0), xytext=(20, 30), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="yellow", ec="b", lw=2),
                            arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(brokenbar_collection, coll_id, ind, x, y):
        annot.xy = (x, y)
        box = brokenbar_collection.get_paths()[ind].get_extents()
        text = f"{ax_gnt.get_yticklabels()[coll_id].get_text()} index:{ind} duration:{box.x1 - box.x0:.0f} "
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.9)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax_gnt:
            for coll_id, brokenbar_collection in enumerate(ax_gnt.collections):
                cont, ind = brokenbar_collection.contains(event)
                if cont:
                    update_annot(brokenbar_collection, coll_id, ind['ind'][0], event.xdata, event.ydata)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    # print("test text")
    plt.show()


def spn_ex(work,job_c,i_at,i_cbt):
    if work == 9:
        job_count=job_c
        at=i_at
        cbt=i_cbt
    else:
        job_count = int(input("job count : "))
        at = []
        cbt = []
        print("please insert your number in order ")
        for x in range(job_count):
            print("insert AT and CBT of job_" + str((int(x) + 1)))
            at.append(int(input("AT: ")))
            cbt.append(int(input("cbt: ")))
    current_time = min(at)
    temp_at = at
    temp_cbt = cbt
    future_at = []
    future_cbt = []
    at_order = []
    cbt_order = []
    job_order = []
    start_time = []
    for x in range(len(at)):
        future_at.append(at[x])
        future_cbt.append(cbt[x])
    x = 1
    if len(temp_at) > 0:
        while x == 1:
            at_index = []
            cbt_index = []
            for y in range(len(at)):
                if temp_at[y] <= current_time:
                    at_index.append(y)
                    cbt_index.append(y)

            working_cbt = []
            working_at = []
            if len(at_index) == 0:
                current_time = current_time + 1
            elif len(at_index) > 0:
                for z in range(len(cbt_index)):
                    i = cbt_index[z]
                    working_cbt.append(temp_cbt[i])
                    working_at.append(temp_at[i])
                needed_cbt = min(working_cbt)
                i_cbt = working_cbt.index(needed_cbt)
                needed_at = working_at[i_cbt]
                at_order.append(needed_at)
                cbt_order.append(needed_cbt)
                start_time.append(current_time)
                for m in range(len(future_cbt)):
                    if needed_at == future_at[m]:
                        for n in range(len(future_cbt)):
                            if needed_cbt == future_cbt[n]:
                                if n not in job_order:
                                    job_order.append(n)

                current_time = current_time + needed_cbt
                temp_at.remove(needed_at)
                temp_cbt.remove(needed_cbt)
            if len(temp_at) == 0:
                x = 0
            working_cbt = []
            working_at = []
    # calculation
    # total time
    tt = 0
    # waiting time=
    wt = 0
    for x in range(len(at_order)):
        jo_number = job_order[x]
        added_time = ((start_time[x] + cbt_order[x]) - start_time[x]) + (start_time[x] - at_order[jo_number])
        tt = tt + added_time
        added_waiting = start_time[x] - at_order[jo_number]
        wt = wt + added_waiting
    if work == 9:
        return tt,(tt/len(at_order)),wt,(wt/len(at_order))
    else:
        print("total time : ", tt)
        print("avg total time : ", tt / len(at_order))
        print("waiting time : ", wt)
        print("avg waiting time : ", wt / len(at_order))
        graphSPN(job_count, future_at, future_cbt, at_order, cbt_order, job_order, start_time)


def HRRN(work,job_c,i_at,i_cbt):
    if work ==9:
        job_count=job_c
        at=i_at
        cbt=i_cbt
        job_number=[]
        for x in range(job_count):

            job_number.append(x)
    else:
        job_count = int(input("job count : "))
        at = []
        cbt = []
        job_number = []
        for x in range(job_count):
            print("insert AT and CBT of job_" + str((int(x) + 1)))
            at.append(int(input("AT: ")))
            cbt.append(int(input("cbt: ")))
            job_number.append(x)
    current_time = min(at)
    temp_at = []
    temp_cbt = []
    temp_job_number = []
    for x in range(job_count):
        temp_at.append(at[x])
        temp_cbt.append(cbt[x])
        temp_job_number.append(job_number[x])

    final_at = []
    final_cbt = []
    final_job_number = []
    current_time_list = []
    number_checker = 0

    deletenum = 0
    for x in range(job_count):
        working_at = []
        working_cbt = []
        working_job_number = []
        while min(temp_at)>current_time:
            current_time=current_time+1
        for y in range(job_count):
            if temp_at[y] <= current_time:
                working_at.append(temp_at[y])
                working_cbt.append(temp_cbt[y])
                working_job_number.append(temp_job_number[y])
        HRRN_list = []
        while min(temp_at)>current_time:
            current_time=current_time+1
        for z in range(len(working_at)):
            checking = (current_time - working_at[z]) / working_cbt[z]
            HRRN_list.append(checking)

        minwork = max(HRRN_list)
        indexSaver = HRRN_list.index(minwork)

        for xx in range(len(working_at)):
            if HRRN_list[xx] >= minwork:
                if working_cbt[xx] < working_cbt[indexSaver]:
                    indexSaver = xx
                    minwork = max((HRRN_list))
        current_time_list.append(current_time)
        current_time = current_time + working_cbt[indexSaver]
        final_at.append(working_at[indexSaver])
        final_cbt.append(working_cbt[indexSaver])
        final_job_number.append(working_job_number[indexSaver])
        l = len(final_job_number)
        temp = len(temp_at)
        for g in range(temp):

            if temp_at[g] == final_at[number_checker]:
                if temp_cbt[g] == final_cbt[number_checker]:
                    if temp_job_number[g] == final_job_number[number_checker]:
                        temp_at[g] = 999999
                        temp_cbt[g] = 9999999
                        temp_job_number[g] = 1999999
                        break
        number_checker = number_checker + 1
    TT = 0
    WT = 0
    for x in range(len(final_at)):
        temp = final_cbt[x] + current_time_list[x]
        temp = temp - final_at[x]
        TT = TT + temp
    for x in range(len(final_at)):
        temp = current_time_list[x] - final_at[x]
        WT = WT + temp
    if work == 9:
        return TT,(TT/len(final_at)),WT,(WT/len(final_at))
    else:
        print("Total time : ", TT)
        print("avg Total Time ", TT / (len(final_at)))
        print("Waiting time : ", WT)
        print("avg Waiting time : ", WT / len(final_at))
        graphHRRN(job_count, final_at, final_cbt, final_job_number, current_time_list)


def RR(work,job_c,i_at,i_cbt,qt):
    if work==9:
        job_count=job_c
        at=i_at
        cbt=i_cbt
        QT=qt
        CS=0
        job_number = []
        for x in range(job_count):
            job_number.append(x)



    elif work == 4:
        job_count = int(input("job count : "))
        QT = int(input("Quantom time : "))
        CS = int(input("Context Switch : "))
    elif work == 1:
        job_count = int(input("job count : "))

    if work!=9:
        at = []
        cbt = []
        job_number = []
        for x in range(job_count):
            print("insert AT and CBT of job_" + str((int(x) + 1)))
            at.append(int(input("AT: ")))
            cbt.append(int(input("cbt: ")))
            job_number.append(x)
    current_time = min(at)
    temp_at = []
    temp_cbt = []
    temp_job_number = []
    if work ==1:
        QT = max(cbt) + 1
        CS = 0


    for x in range(job_count):
        temp_at.append(at[x])
        temp_cbt.append(cbt[x])
        temp_job_number.append(job_number[x])
    final_at = []
    final_cbt = []
    final_job_number = []
    fina1_current_time = []
    number_checker = 0
    x = 0
    while x == 0:
        while min(temp_at)>current_time:
            current_time=current_time+1
        working_at = min(temp_at)
        index_at = temp_at.index(working_at)
        working_cbt = temp_cbt[index_at]
        working_job_number = temp_job_number[index_at]
        if working_cbt <= QT:
            final_at.append(working_at)
            final_cbt.append(working_cbt)
            final_job_number.append(working_job_number)
            fina1_current_time.append(current_time)
            current_time = current_time + working_cbt + CS
            temp_at.pop(index_at)
            temp_cbt.pop(index_at)
            temp_job_number.pop(index_at)
        elif working_cbt > QT:
            final_at.append(working_at)
            final_cbt.append(QT)
            final_job_number.append(working_job_number)
            fina1_current_time.append(current_time)
            current_time = current_time + QT + CS
            temp_at.pop(index_at)
            temp_cbt.pop(index_at)
            temp_job_number.pop(index_at)
            temp_at.append(current_time)
            temp_cbt.append(working_cbt - QT)
            temp_job_number.append(working_job_number)
        if len(temp_at) == 0:
            x = 1
    l = len(fina1_current_time)
    TT = 0
    WT = 0
    for y in range(job_count):
        for z in range(len(final_at)):
            if final_job_number[z] == y:
                TT = TT + (fina1_current_time[z] - final_at[z]) + final_cbt[z]
                WT = WT + (fina1_current_time[z] - final_at[z] + CS)
    WT = WT - (2 * (CS))
    if work == 9:
        return TT,(TT/job_count),WT,(WT/job_count)
    else:
        print("Total time : ", TT)
        print("avg Total time : ", TT / job_count)
        print("Waiting time : ", WT)
        print("avg Waiting time :  ", WT / job_count)

        graphRR(job_count, final_at, final_cbt, final_job_number, fina1_current_time, QT)


def SRTF(work,job_c,i_at,i_cbt):
    if work==9:
        job_count=job_c
        at=i_at
        cbt=i_cbt
        CS=0
        job_number=[]

        for x in range(job_count):
            job_number.append(x)
    else:
        job_count = int(input("job count : "))
        CS = int(input("Context Switch : "))

        at = []
        cbt = []
        job_number = []
        for x in range(job_count):
            print("insert AT and CBT of job_" + str((int(x) + 1)))
            at.append(int(input("AT: ")))
            cbt.append(int(input("cbt: ")))
            job_number.append(x)
    current_time = min(at)
    real_current_time = min(at)
    temp_current_time = min(at)
    temp_at = []
    temp_cbt = []
    temp_job_number = []
    for x in range(job_count):
        temp_at.append(at[x])
        temp_cbt.append(cbt[x])
        temp_job_number.append(job_number[x])
    final_at = []
    final_cbt = []
    final_job_number = []
    fina1_current_time = []
    number_checker = 0

    x = 0
    while x == 0:
        working_cbt = []
        working_at = []
        working_job_number = []
        while min(temp_at)>real_current_time:
            real_current_time=real_current_time+1
        for y in range(len(temp_at)):
            if real_current_time >= temp_at[y]:
                working_cbt.append(temp_cbt[y])
                working_at.append(temp_at[y])
                working_job_number.append(temp_job_number[y])

        using_cbt = min(working_cbt)
        index_used = working_cbt.index(using_cbt)
        using_at = working_at[index_used]
        using_job_number = working_job_number[index_used]

        temp_check_at = []
        temp_check_cbt = []
        temp_check_job_number = []
        temp_current_time = temp_current_time + using_cbt
        counter = 0
        checker = False
        flag = False
        while checker == False:
            if current_time == temp_current_time:
                checker = True
            counter = counter + 1
            current_time = current_time + 1
            for z in range(len(temp_at)):
                if temp_at[z] == current_time:
                    if temp_cbt[z] < using_cbt - counter:
                        final_at.append(using_at)
                        final_cbt.append(counter)
                        final_job_number.append(using_job_number)
                        fina1_current_time.append(real_current_time)
                        real_current_time = real_current_time + counter
                        checker = True
                        flag = True
                        temp_at.append(real_current_time)
                        temp_cbt.append(using_cbt - counter)
                        temp_job_number.append(using_job_number)

                        for qq in range(len(temp_at)):
                            if temp_at[qq] == using_at:
                                if temp_cbt[qq] == using_cbt:
                                    if temp_job_number[qq] == using_job_number:
                                        temp_at.pop(qq)
                                        temp_cbt.pop(qq)
                                        temp_job_number.pop(qq)
                                        break
        if flag == False:
            final_at.append(using_at)
            final_cbt.append(using_cbt)
            final_job_number.append(using_job_number)
            fina1_current_time.append(real_current_time)
            for qq in range(len(temp_at)):
                if temp_at[qq] == using_at:
                    if temp_cbt[qq] == using_cbt:
                        if temp_job_number[qq] == using_job_number:
                            temp_at.pop(qq)
                            temp_cbt.pop(qq)
                            temp_job_number.pop(qq)
                            break

            real_current_time = real_current_time + using_cbt
        if len(temp_at) == 0:
            x = 1

    CS_Added = []
    for x in range(len(fina1_current_time)):
        y = (fina1_current_time[x])
        if x>0:
            if (fina1_current_time[x-1]+CS+final_cbt[x-1])<y:
                z=(CS*0)
            else:
                z = (CS) * x

        CS_Added.append(y + z)

    TT = 0
    WT = 0

    for y in range(job_count):
        for z in range(len(final_at)):
            if final_job_number[z] == y:
                TT = TT + (CS_Added[z] - final_at[z]) + final_cbt[z]
                WT = WT + (CS_Added[z] - final_at[z])
    if work == 9:
        return TT,(TT/job_count),WT,(WT/job_count)
    else:
        print("Total time : ", TT)
        print("avg Total time : ", TT / job_count)
        print("Waiting time : ", WT)
        print("avg Waiting time :  ", WT / job_count)
        graphRR(job_count, final_at, final_cbt, final_job_number, CS_Added, max(final_cbt))


print("which scheduler you want to use")
print("exclusive FCFS:1      SPN:2    HRRN:3 ")
print("non Exclusive RR:4    SRTF : 5    ")
print("if you want compare which method is the best enter 6 ")
job_type = int(input("enter your request : "))
if job_type == 1:
    RR(1,0,0,0,0)
elif job_type == 2:
    spn_ex(0,0,0,0)
elif job_type == 3:
    HRRN(0,0,0,0)
elif job_type == 4:
    RR(4,0,0,0,0)
elif job_type == 5:
    SRTF(0,0,0,0)
elif job_type ==6:
    job_count = int(input("job count : "))
    at1 = []
    cbt1 = []
    at2 = []
    cbt2 = []
    at3 = []
    cbt3 = []
    at4 = []
    cbt4 = []
    at5=[]
    cbt5=[]
    job_number = []
    QT=int(input("insert Quantom time : "))
    for x in range(job_count):
        print("insert AT and CBT of job_" + str((int(x) + 1)))
        w1=(int(input("AT: ")))
        w2=(int(input("cbt: ")))
        at1.append(w1)
        cbt1.append(w2)
        at2.append(w1)
        cbt2.append(w2)
        at3.append(w1)
        cbt3.append(w2)
        at4.append(w1)
        cbt4.append(w2)
        at5.append(w1)
        cbt5.append(w2)


        job_number.append(x)
    """
    n1,n2,n3,n4=RR(9,job_count,at1,cbt1,max(cbt1))
    print("Job type : FCFS " , " Total Time : " , n1 , " avg Total time : " , n2 , " Waiting time : " , n3 , "avg waiting time : " , n4)
    n1,n2,n3,n4=spn_ex(9,job_count,at2,cbt2)
    print("Job type : SPN " , " Total Time : " , n1 , " avg Total time : " , n2 , " Waiting time : " , n3 , "avg waiting time : " , n4)
    n1,n2,n3,n4=RR(9,job_count,at3,cbt3,QT)
    print("Job type : Round Robin " , " Total Time : " , n1 , " avg Total time : " , n2 , " Waiting time : " , n3 , "avg waiting time : " , n4)
    n1,n2,n3,n4=SRTF(9,job_count,at4,cbt4)
    print("Job type : SRTF " , " Total Time : " , n1 , " avg Total time : " , n2 , " Waiting time : " , n3 , "avg waiting time : " , n4)
    """
    n11,n12,n13,n14=RR(9,job_count,at1,cbt1,max(cbt1))
    n21,n22,n23,n24=spn_ex(9,job_count,at2,cbt2)
    n31,n32,n33,n34=HRRN(9,job_count,at3,cbt3)
    n41,n42,n43,n44=RR(9,job_count,at4,cbt4,QT)
    n51,n52,n53,n54=SRTF(9,job_count,at5,cbt5)
    data = [["FCFS " , n11,n12,n13,n14],["SPN",n21,n22,n23,n24],["HRRN",n31,n32,n33,n34],["RR",n41,n42,n43,n44],["SRTF",n51,n52,n53,n54]]
    print(tabulate(data,headers=["job type",'Total Time ', 'avg TT ' , "Waiting time " , "avg WT"]))

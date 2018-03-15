
def make_html(song_name, num):
    scripts = '''
    <b>入力信号 "{song_name}" (DSD100 0{num})</b><br>

    <table>
        <tr>
            <td width=400>
                    入力信号<br>(Bass, Vocals)<br>
    <audio src="./src/mix_3{num}.mp3" preload="auto"></audio>
            </td>
        </tr>
    </table>
    <br>

    <b>Duong+DNNによる分離信号</b><br>
    <table>
        <tr>
            <td>分離信号 1<br>(Bass)<br>
    <audio src="./src/bass_3{num}_duongdnn.mp3" preload="auto"></audio>
            </td>
            <td>分離信号 2<br>(Vocals)<br>
    <audio src="./src/vocals_3{num}_duongdnn.mp3" preload="auto"></audio>
            </td>
        </tr>
    </table>

    <br>

    <b>DNN+WFによる分離信号</b><br>
    <table>
        <tr>
            <td>分離信号 1<br>(Bass)<br>
    <audio src="./src/3{num}_bass_wf.mp3" preload="auto"></audio>
            </td>
            <td>分離信号 2<br>(Vocals)<br>
    <audio src="./src/3{num}_vocals_wf.mp3" preload="auto"></audio>
            </td>
        </tr>
    </table>

    <br>

    <b>ILRMAによる分離信号</b><br>
    <table>
        <tr>
            <td>分離信号 1<br>(Bass)<br>
    <audio src="./src/bass_3{num}_ILRMA.mp3" preload="auto"></audio>
            </td>
            <td>分離信号 2<br>(Vocals)<br>
    <audio src="./src/vocals_3{num}_ILRMA.mp3" preload="auto"></audio>
            </td>
        </tr>
    </table>

    <br>

    <b>IDLMAによる分離信号</b><br>
    <table>
        <tr>
            <td>分離信号 1<br>(Bass)<br>
    <audio src="./src/bass_3{num}_idlma.mp3" preload="auto"></audio>
            </td>
            <td>分離信号 2<br>(Vocals)<br>
    <audio src="./src/vocals_3{num}_idlma.mp3" preload="auto"></audio>
            </td>
        </tr>
    </table>

    <br>
    <div style="border:1px solid;margin:5px;"></div>
    '''.format(song_name=song_name, num='{:02d}'.format(num))
    print(scripts)


make_html('ANiMAL - Clinic A', 1)
make_html('ANiMAL - Rockshow', 2)
make_html('Actions - One Minute Smile', 3)
make_html('Al James - Schoolboy Facination', 4)
make_html('Angela Thomas Wade - Milk Cow Blues', 5)
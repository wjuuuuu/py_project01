import streamlit as st


# 设置页面配置项
import streamlit as st

st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://chatgpt.com/',
        'Report a bug': "https://www.chatgpt.com/",
        'About': "# 这是一个 Streamlit 的入门页面～"
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("缅因猫是一种体型巨大、气质高贵的长毛猫，被称为“温柔的巨人”。它们拥有强壮的身体、浓密蓬松的毛发、修长的尾巴以及标志性的耳尖毛簇，看起来像一只来自森林中的小型野兽。厚实的皮毛能够帮助它们适应寒冷环境，而威严的外表也让它们散发出独特的王者气息。")
st.write("尽管体型庞大，缅因猫的性格却十分温和友善。它们聪明、忠诚，喜欢与人互动，经常会像狗狗一样跟随主人，在家中陪伴左右。它们不会过分吵闹，叫声反而细腻轻柔，有时会发出独特的“咕噜”声与主人交流，让人感受到它们温柔的一面。")
st.write("阳光洒落时，缅因猫厚重的毛发随风轻轻摆动，巨大的身躯显得威风又优雅。它们或慵懒地躺在沙发上，或端坐在窗边观察世界，既拥有野性的魅力，又保留着亲人的温暖。作为世界上最大的家猫品种之一，缅因猫凭借霸气的外表和温柔的内心，成为许多人心中理想的“猫中巨人”。")

# 图片
st.image("./resources/cat.jpg")

# 音频
st.audio("./resources/青花瓷.flac")

# 视频
st.video("./resources/集锦.mp4")

# logo
st.logo("./resources/logo.png")

# 表格
student_date = {
    "姓名" : ["wujie", "wujie2", "wujie3"],
    "学号" : ["20230001", "20230002", "20230003"],
    "语文" : [98, 95, 92],
    "数学" : [90, 88, 94],
    "英语" : [95, 92, 98],
    "总成绩" : [283, 275, 280]
}
st.table(student_date)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名：")
st.write(f"您输入的姓名为：{name}")

# 密码输入框
password = st.text_input("请输入密码：", type="password")
st.write(f"您输入的密码为：{password}")

# 单选框
gender = st.radio("请选择您的性别：", ["男", "女","未知"], index = 1)
st.write(f"您选择的性别为：{gender}")
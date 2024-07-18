import streamlit as st
# from http import HTTPStatus
from dashscope import Application

# 直接在代码中硬编码API密钥（不推荐，仅供测试使用）
api_key = 'sk-cdf976f2ae78411288dfec1fee87717e'

st.title("💬 经管一核两翼智能助手")

# 初始化会话状态
session_state = st.session_state
if 'session_id' not in session_state:
    session_state['session_id'] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "请提出您的问题。"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def fetch_data_from_bailian(query, session_id=None):
    # 使用上一次的session_id，如果没有则为None
    response = Application.call(
        app_id='55f75f83f52248c5a2aed6e23c398883',
        prompt=query,
        api_key=api_key,
        session_id=session_id  # 添加session_id参数
    )

    # if response.status_code == HTTPStatus.OK:
        # 更新session_id以供下一次调用使用
    session_state['session_id'] = response.output.session_id
    return response
    # else:
    #     st.error(f'请求失败，状态码：{response.status_code}')
    #     return None


if prompt := st.chat_input():
    if prompt:
        # st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        data = fetch_data_from_bailian(prompt, session_state['session_id'])
        # messages = st.session_state.messages
        # msg = message.output.content
        # st.session_state.messages.append({"role": "assistant", "content": msg})
        # 在聊天界面展示助手的回复。
        st.chat_message("assistant").write(data.output.text)
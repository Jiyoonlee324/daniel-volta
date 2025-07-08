import streamlit as st
import matplotlib.pyplot as plt

# 제목
st.title("전기화학 전지 시각화 비교 프로그램")

# 전지 선택
cell_type = st.radio("전지 종류를 선택하세요:", ["다니엘 전지", "볼타 전지"])

# 그래프 함수
def draw_cell_diagram(cell_type):
    fig, ax = plt.subplots(figsize=(7,4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # 공통 요소: 전극 위치 표시
    ax.text(1, 4.5, "Zn 전극 (-극)", fontsize=10)
    ax.text(8, 4.5, "Cu 전극 (+극)", fontsize=10)
    ax.plot([1, 1], [1, 4], color='gray', linewidth=8)
    ax.plot([8, 8], [1, 4], color='orange', linewidth=8)

    ax.arrow(2.5, 3, 4, 0, head_width=0.3, head_length=0.5, fc='blue', ec='blue')
    ax.text(5, 3.3, "전자 흐름", fontsize=10)

    if cell_type == "다니엘 전지":
        ax.text(1, 0.5, "Zn → Zn²⁺ + 2e⁻ (산화)", fontsize=10)
        ax.text(7, 0.5, "Cu²⁺ + 2e⁻ → Cu (환원)", fontsize=10)
        ax.text(4, 4.7, "염다리: Na⁺, Cl⁻ 이동", fontsize=10, color='green')

        ax.annotate("Zn²⁺ ↑", (1.2, 2.5), color='purple')
        ax.annotate("Cu²⁺ ↓", (7.7, 2.5), color='purple')

    elif cell_type == "볼타 전지":
        ax.text(1, 0.5, "Zn + H⁺ → Zn²⁺ + H₂↑ (산화)", fontsize=10)
        ax.text(7, 0.5, "2H⁺ + 2e⁻ → H₂ (환원)", fontsize=10)
        ax.text(4, 4.7, "H₂SO₄ 용액 내 H⁺", fontsize=10, color='green')

        ax.annotate("H₂ 기체 ↑", (8.2, 2.5), color='purple')
        ax.annotate("Zn²⁺ ↑", (1.2, 2.5), color='purple')

    return fig

# 설명 출력
if cell_type == "다니엘 전지":
    st.subheader("다니엘 전지 설명")
    st.markdown("""
    - **구성**: Zn | Zn²⁺ || Cu²⁺ | Cu  
    - **전해질**: ZnSO₄, CuSO₄  
    - **염다리**: 두 용액 사이 이온 평형 유지  
    - **전자 흐름**: Zn → Cu  
    - **에너지 변환**: 화학 에너지 → 전기 에너지
    """)

elif cell_type == "볼타 전지":
    st.subheader("볼타 전지 설명")
    st.markdown("""
    - **구성**: Zn | H₂SO₄ 용액 | Cu  
    - **전해질**: 묽은 황산  
    - **염다리 없음** (H⁺ 이온이 직접 참여)  
    - **전자 흐름**: Zn → Cu  
    - **산화 환원 반응**: H⁺가 환원되어 H₂ 기체 발생
    """)

# 그림 출력
fig = draw_cell_diagram(cell_type)
st.pyplot(fig)

# 비교 설명
st.subheader("다니엘 전지 vs 볼타 전지 차이점")

st.markdown("""
| 구분 | 다니엘 전지 | 볼타 전지 |
|------|-------------|-----------|
| **전해질** | 두 종류 (ZnSO₄, CuSO₄) | 하나 (묽은 H₂SO₄) |
| **염다리** | 있음 | 없음 |
| **환원 반응** | Cu²⁺ + 2e⁻ → Cu | 2H⁺ + 2e⁻ → H₂ |
| **생성물** | 고체 Cu 석출 | H₂ 기체 발생 |
| **사용 가능성** | 이론적 모델, 실제 사용 | 역사적 실험 전지 |
""")

---

## ✅ 실행 방법 (Python 환경에서)

```bash
pip install streamlit matplotlib
streamlit run app.py

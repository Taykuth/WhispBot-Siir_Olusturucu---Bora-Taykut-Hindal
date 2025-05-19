import streamlit as st

# Etiketli şiir corpus'u
corpus = {
    "aşk": [
        "kalbim gülüşünde umut kalbim",
        "kalbim sana her başlar",
        "her gülüşünde umut dost",
        "kalbim yankılanır tek başıma"
    ],
    "umut": [
        "umuda doğru bir adım at",
        "gökkuşağı gibi içimde renkler",
        "her yeni gün yeni bir başlangıç",
        "karanlığı deler umutla kalbim"
    ],
    "yalnızlık": [
        "geceye düşünce bir başıma kaldım",
        "duvarlarla konuşan gölgem var",
        "sokak lambası altında sessizliğim",
        "yalnızlık bana kendini anlatır"
    ],
    "mutluluk": [
        "gülüşünle başlar her yeni sabah",
        "güz mevsimi gibi içimde huzur",
        "bir şarkı söylerim şehirle birlikte",
        "mutluluk dolu adımlar gökyüzüne"
    ],
    "kızgınlık": [
        "sözlerim yangın gibi dudaklarımda",
        "içimde bir volkan patlamaya hazır",
        "sessizlik bile öfkeyle yoğrulur",
        "gözlerimde şamdan gibi parlayan hırs"
    ]
}

st.title("Şiirli Duygulara Giriş - Şiir Botu")
st.write("A\u015fa\u011f\u0131daki duygu t\u00fcrlerinden birini se\u00e7erek ona g\u00f6re yaz\u0131lm\u0131\u015f 4 sat\u0131rl\u0131k \u015fiirleri g\u00f6rebilirsiniz.")

secilen = st.selectbox("\u015eiiir i\u00e7in bir duygu se\u00e7in:", list(corpus.keys()))

if st.button("\u015eiiri G\u00f6ster"):
    st.markdown(f"### [{secilen}]")
    for m in corpus[secilen]:
        st.markdown(f"- {m}")

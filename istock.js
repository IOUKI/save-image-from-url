// istock 網站圖片爬蟲

let sleepSetTimeout_ctrl;

function sleep(ms) {
    clearInterval(sleepSetTimeout_ctrl);
    return new Promise(resolve => sleepSetTimeout_ctrl = setTimeout(resolve, ms));
}

async function main() {
    const totalPage = parseInt(document.getElementsByClassName('EEuNOdJESEP1DykbrGuZ')[0].innerHTML)
    const nextButton = document.getElementsByClassName('sgteZ8IeHi_1YN4npuIQ LKeCllp5T38Hwu_jsBoh')[0]

    let urlArr = []
    for (let i = 0; i <= totalPage; i++) {
        // 滾動視窗，載入圖片
        window.scrollTo(0, document.body.scrollHeight)
        
        await sleep(500)

        // 取得圖片url
        const imageClassName = 'yGh0CfFS4AMLWjEE9W7v'
        let doms = document.getElementsByClassName(imageClassName)
        for (let j = 0; j < doms.length; j++) {
            urlArr.push(doms[j].src)
        }

        await sleep(500)

        // 換下一頁
        nextButton.click()

        console.log(urlArr)
    }

}

main()
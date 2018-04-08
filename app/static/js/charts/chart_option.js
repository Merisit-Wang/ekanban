
function chartOption(chartData, chartName) {
    var option = {
    title : {
        text:chartName,
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    calculable : true,
    series : [
        {
            name:'半径模式',
            type:'pie',
            radius : [10, 150],
            center : ['50%', '50%'],
            roseType : 'radius',
            label: {
                normal: {
                    show: true,
                    formatter: '{b}: {c}({d}%)'
                },
                emphasis: {
                    show: true
                }
            },
            lableLine: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: true
                }
            },
            data:chartData
        }
    ]
};

    return option;
}

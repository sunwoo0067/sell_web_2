// 시스템 메트릭스 차트 초기화
const systemCtx = document.getElementById('systemMetricsChart').getContext('2d');
const systemChart = new Chart(systemCtx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'CPU 사용률',
            data: [],
            borderColor: 'rgb(75, 192, 192)',
        }, {
            label: '메모리 사용률',
            data: [],
            borderColor: 'rgb(255, 99, 132)',
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        }
    }
});

// 상품 처리 현황 차트 초기화
const productCtx = document.getElementById('productMetricsChart').getContext('2d');
const productChart = new Chart(productCtx, {
    type: 'bar',
    data: {
        labels: ['성공', '실패', '처리 중'],
        datasets: [{
            label: '상품 처리 현황',
            data: [0, 0, 0],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgb(75, 192, 192)',
                'rgb(255, 99, 132)',
                'rgb(255, 206, 86)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// 실시간 데이터 업데이트
async function updateMetrics() {
    try {
        const response = await fetch('/api/monitoring/metrics');
        const data = await response.json();

        // 시스템 메트릭스 업데이트
        const timestamp = new Date().toLocaleTimeString();
        systemChart.data.labels.push(timestamp);
        systemChart.data.datasets[0].data.push(data.system.cpu_usage);
        systemChart.data.datasets[1].data.push(data.system.memory_usage);

        // 최근 10개 데이터만 표시
        if (systemChart.data.labels.length > 10) {
            systemChart.data.labels.shift();
            systemChart.data.datasets.forEach(dataset => dataset.data.shift());
        }

        systemChart.update();

        // 상품 처리 현황 업데이트
        productChart.data.datasets[0].data = [
            data.performance.total_processed,
            data.performance.total_failed,
            data.performance.processing_count
        ];
        productChart.update();

        // 작업 목록 업데이트
        updateTaskTable(data.performance.recent_tasks);

    } catch (error) {
        console.error('Error updating metrics:', error);
    }
}

// 작업 목록 테이블 업데이트
function updateTaskTable(tasks) {
    const tbody = document.querySelector('#taskTable tbody');
    tbody.innerHTML = '';

    tasks.forEach(task => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${task.id}</td>
            <td>${task.product_name}</td>
            <td><span class="badge bg-${getStatusColor(task.status)}">${task.status}</span></td>
            <td>${task.processing_time}s</td>
            <td>${task.result}</td>
        `;
        tbody.appendChild(row);
    });
}

function getStatusColor(status) {
    switch (status) {
        case 'completed': return 'success';
        case 'failed': return 'danger';
        case 'processing': return 'warning';
        default: return 'secondary';
    }
}

// 1초마다 메트릭스 업데이트
setInterval(updateMetrics, 1000);
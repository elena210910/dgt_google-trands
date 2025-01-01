import plotly.graph_objects as go
from plotly.subplots import make_subplots
.....

# Creación de tres gráficos en una sola página
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "Interés en Google Trends: Toyota", "Matriculaciones Toyota",
        "Interés en Google Trends: Renault", "Matriculaciones Renault",
        "Interés en Google Trends: KIA", "Matriculaciones KIA"
    )
)

# Gráfico de interés en Google Trends para Toyota
fig.add_trace(
    go.Scatter(
        x=google_trends_data['date'],
        y=google_trends_data['Toyota'],
        mode='lines+markers',
        name='Interés en Google Trends: Toyota',
        line=dict(color='cyan')
    ),
    row=1, col=1
)

# Gráfico de ventas de Toyota
fig.add_trace(
    go.Scatter(
        x=sales_toyota['Fecha'],
        y=sales_toyota['sales_toyota'],
        mode='lines+markers',
        name='Matriculaciones Toyota',
        line=dict(color='orange')
    ),
    row=1, col=2
)

# Gráfico de interés en Google Trends para Renault
fig.add_trace(
    go.Scatter(
        x=google_trends_data['date'],
        y=google_trends_data['Renault'],
        mode='lines+markers',
        name='Interés en Google Trends: Renault',
        line=dict(color='blue')
    ),
    row=2, col=1
)

# Gráfico de ventas de Renault
fig.add_trace(
    go.Scatter(
        x=sales_renault['Fecha'],
        y=sales_renault['sales_renault'],
        mode='lines+markers',
        name='Matriculaciones Renault',
        line=dict(color='green')
    ),
    row=2, col=2
)

# Gráfico de interés en Google Trends para KIA
fig.add_trace(
    go.Scatter(
        x=google_trends_data['date'],
        y=google_trends_data['KIA'],
        mode='lines+markers',
        name='Interés en Google Trends: KIA',
        line=dict(color='purple')
    ),
    row=3, col=1
)

# Gráfico de ventas de KIA
fig.add_trace(
    go.Scatter(
        x=sales_kia['Fecha'],
        y=sales_kia['sales_kia'],
        mode='lines+markers',
        name='Matriculaciones KIA',
        line=dict(color='red')
    ),
    row=3, col=2
)

# Configuración del diseño
fig.update_layout(
    title='Interés en Google Trends y Matriculaciones en DGT de Toyota, Renault y KIA los dias 02.12.2024 hasta 26.12.2024',
    template='plotly_dark',
    showlegend=False
)

# Mostrar gráficos
fig.show()

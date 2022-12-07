import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import numpy as np
import joblib
 
#Font family load
external_stylesheets = ['https://fonts.googleapis.com/css2?family=Space+Mono&display=swap']  
#Start app
app = dash.Dash(__name__)
app.title = 'HCM House Price Prediction'
#For deployment
server = app.server
#App layout
app.layout = html.Div(
    children=[
        html.Div(
            [
                html.H1(
                    'HO CHI MINH CITY HOUSE PRICE PREDICTION'
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    'LAND AREA (m2)', style={'color':'#c86d53'}, className='area-title'
                                ),
                                html.Div(
                                    '(Diện Tích Đất)', style={'color':'#c86d53'}, className='area-title-vn'
                                ),
                                dcc.Input(
                                    id='area',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '90%',
                                        'textAlign': 'center'
                                    },
                                    className='area-selected'
                                ),
                                html.Div(id='area-output')
                            ], className='area-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'LAND USED AREA (m2)', style={'color':'#c86d53'}, className='area-used-title'
                                ),
                                html.Div(
                                    '(Diện Tích Đất Sử Dụng)', style={'color':'#c86d53'}, className='area-used-title-vn'
                                ),
                                dcc.Input(
                                    id='area-used',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '90%',
                                        'textAlign': 'center'
                                    },
                                    className='area-used-selected'
                                ),
                                html.Div(id='area-used-output')
                            ], className='area-used-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'ALLEY WIDTH (m)', style={'color':'#c86d53'}, className='alley-width-title'
                                ),
                                html.Div(
                                    '(Độ Rộng Hẻm)', style={'color':'#c86d53'}, className='alley-width-title-vn'
                                ),
                                dcc.Input(
                                    id='alley-width',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '90%',
                                        'textAlign': 'center'
                                    },
                                    className='alley-width-selected'
                                ),
                                html.Div(id='alley-width-output')
                            ], className='alley-width-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'WIDTH (m)', style={'color':'#c86d53'}, className='width-title'
                                ),
                                html.Div(
                                    '(Chiều Rộng)', style={'color':'#c86d53'}, className='width-title-vn'
                                ),
                                dcc.Input(
                                    id='width',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '90%',
                                        'textAlign': 'center'
                                    },
                                    className='width-selected'
                                ),
                                html.Div(id='width-output')
                            ], className='width-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'NUMBER BEDROOM', style={'color':'#c86d53'}, className='bedroom-title'
                                ),
                                html.Div(
                                    '(Số Phòng Ngủ)', style={'color':'#c86d53'}, className='bedroom-title-vn'
                                ),
                                dcc.Input(
                                    id='bedroom',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '90%',
                                        'textAlign': 'center'
                                    },
                                    className='bedroom-selected'
                                ),
                                html.Div(id='bedroom-output')
                            ], className='bedroom-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'NUMBER FLOOR', style={'color':'#c86d53'}, className='floor-title'
                                ),
                                html.Div(
                                    '(Số Tầng)', style={'color':'#c86d53'}, className='floor-title-vn'
                                ),
                                dcc.Input(
                                    id='floor',
                                    type='number',
                                    placeholder='Enter the value here',
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono',
                                        'width' : '85%',
                                        'textAlign': 'center'
                                    },
                                    className='floor-selected'
                                ),
                                html.Div(id='floor-output')
                            ], className='floor-division'
                        )
                    ], className='container-left-under'
                )
            ], className='container-left'
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    'DISTRICT', style={'color':'#c86d53'}, className='district-title'
                                ),
                                html.Div(
                                    '(Quận, Huyện)', style={'color':'#c86d53'}, className='district-title-vn'
                                ),
                                dcc.Dropdown(
                                    id='district',
                                    options=[
                                        {'label': 'District 1 (Quận 1)', 'value': 'q1'},
                                        {'label': 'District 2 (Quận 2)', 'value': 'q2'},
                                        {'label': 'District 3 (Quận 3)', 'value': 'q3'},
                                        {'label': 'District 4 (Quận 4)', 'value': 'q4'},
                                        {'label': 'District 5 (Quận 5)', 'value': 'q5'},
                                        {'label': 'District 6 (Quận 6)', 'value': 'q6'},
                                        {'label': 'District 7 (Quận 7)', 'value': 'q7'},
                                        {'label': 'District 8 (Quận 8)', 'value': 'q8'},
                                        {'label': 'District 9 (Quận 9)', 'value': 'q9'},
                                        {'label': 'District 10 (Quận 10)', 'value': 'q10'},
                                        {'label': 'District 11 (Quận 11)', 'value': 'q11'},
                                        {'label': 'District 12 (Quận 12)', 'value': 'q12'},
                                        {'label': 'District Binh Tan (Quận Bình Tân)', 'value': 'binh-tan'},
                                        {'label': 'District Thu Duc (Quận Thủ Đức)', 'value': 'thu-duc'},
                                        {'label': 'District Binh Thanh (Quận Bình Thạnh)', 'value': 'binh-thanh'},
                                        {'label': 'District Tan Phu (Quận Tân Phú)', 'value': 'tan-phu'},
                                        {'label': 'District Tan Binh (Quận Tân Bình)', 'value': 'tan-binh'},
                                        {'label': 'District Phu Nhuan (Quận Phú Nhuận)', 'value': 'phu-nhuan'},
                                        {'label': 'District Go Vap (Quận Gò Vấp)', 'value': 'go-vap'},
                                        {'label': 'District Hoc Mon (Huyện Hóc Môn)', 'value': 'hoc-mon'},
                                        {'label': 'District Nha Be (Huyện Nhà Bè)', 'value': 'nha-be'},
                                        {'label': 'District Binh Chanh (Huyện Bình Chánh)', 'value': 'binh-chanh'}
                                    ],
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono'
                                    },
                                    placeholder='Select a district',
                                    className='district-selected'
                                ),
                                html.Div(id='district-output')
                            ], className='district-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'CATEGORY', style={'color':'#c86d53'}, className='category-title'
                                ),
                                html.Div(
                                    '(Phân Loại)', style={'color':'#c86d53'}, className='category-title-vn'
                                ),
                                dcc.Dropdown(
                                    id='category',
                                    options=[
                                        {'label': 'Home (Nhà Ở)', 'value': 'nha'},
                                        {'label': 'Condominium (Căn Hộ)', 'value': 'can-ho'},
                                        {'label': 'Town House (Nhà Mặt Tiền)', 'value': 'nha-mat-tien'},
                                        {'label': 'Boarding House (Dãy Trọ)', 'value': 'day-tro'},
                                        {'label': 'Hotel/Villa (Khách Sạn/Villa)', 'value': 'villa'},
                                    ],
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono'
                                    },
                                    placeholder='Select a category',
                                    className='category-selected'
                                ),
                                html.Div(id='category-output')
                            ], className='category-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'HOUSE DIRECTION', style={'color':'#c86d53'}, className='direction-title'
                                ),
                                html.Div(
                                    '(Hướng Nhà)', style={'color':'#c86d53'}, className='direction-title-vn'
                                ),
                                dcc.Dropdown(
                                    id='direction',
                                    options=[
                                        {'label': 'North (Bắc)', 'value': 'bac'},
                                        {'label': 'South (Nam)', 'value': 'nam'},
                                        {'label': 'West (Tây)', 'value': 'tay'},
                                        {'label': 'East (Đông)', 'value': 'dong'},
                                        {'label': 'Others (Khác)', 'value': 'khac'}
                                    ],
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono'
                                    },
                                    placeholder='Select a direction',
                                    className='direction-selected'
                                ),
                                html.Div(id='direction-output')
                            ], className='direction-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'HOUSE STATUS', style={'color':'#c86d53'}, className='status-title'
                                ),
                                html.Div(
                                    '(Trạng Thái)', style={'color':'#c86d53'}, className='status-title-vn'
                                ),
                                dcc.Dropdown(
                                    id='status',
                                    options=[
                                        {'label': 'Empty (Để Trống)', 'value': 'de-trong'},
                                        {'label': 'Living (Đang Ở)', 'value': 'dang-o'},
                                        {'label': 'Renting (Đang Cho Thuê)', 'value': 'dang-cho-thue'},
                                        {'label': 'Others (Khác)', 'value': 'khac'}
                                    ],
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono'
                                    },
                                    placeholder='Select a status',
                                    className='status-selected'
                                ),
                                html.Div(id='status-output')
                            ], className='status-division'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    'HOUSE VERIFICATION', style={'color':'#c86d53'}, className='verification-title'
                                ),
                                html.Div(
                                    '(Giấy Tờ)', style={'color':'#c86d53'}, className='verification-title-vn'
                                ),
                                dcc.Dropdown(
                                    id='verification',
                                    options=[
                                        {'label': 'Pink Book (Sổ Hồng)', 'value': 'so-hong'},
                                        {'label': 'Red Book (Sổ Đỏ)', 'value': 'so-do'},
                                        {'label': 'District Certificate (Giấy Chứng Nhận Phường)', 'value': 'giay-chung-nhan-phuong'},
                                        {'label': 'Others (Khác)', 'value': 'khac'}
                                    ],
                                    style={
                                        'background-color': '#f5ead0',
                                        'border-color': '#f5ead0',
                                        'font-family':'Space Mono'
                                    },
                                    placeholder='Select a verification',
                                    className='verification-selected'
                                ),
                                html.Div(id='verification-output')
                            ], className='verification-division'
                        )
                    ], className='container-right-above'
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            'HAVE MEZZANINE', style={'color':'#c86d53'}, className='mezzanine-title'
                                        ),
                                        html.Div(
                                            '(Có Gác Lửng)', style={'color':'#c86d53'}, className='mezzanine-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='mezzanine',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='mezzanine-selected'
                                        ),
                                        html.Div(id='mezzanine-output')
                                    ], className='mezzanine-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'HAVE ROOFTOP', style={'color':'#c86d53'}, className='rooftop-title'
                                        ),
                                        html.Div(
                                            '(Có Sân Thượng)', style={'color':'#c86d53'}, className='rooftop-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='rooftop',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='rooftop-selected'
                                        ),
                                        html.Div(id='rooftop-output')
                                    ], className='rooftop-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'HAVE BASEMENT', style={'color':'#c86d53'}, className='basement-title'
                                        ),
                                        html.Div(
                                            '(Có Tầng Hầm)', style={'color':'#c86d53'}, className='basement-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='basement',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='basement-selected'
                                        ),
                                        html.Div(id='basement-output')
                                    ], className='basement-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'HAVE ATTIC', style={'color':'#c86d53'}, className='attic-title'
                                        ),
                                        html.Div(
                                            '(Có Áp Mái)', style={'color':'#c86d53'}, className='attic-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='attic',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='attic-selected'
                                        ),
                                        html.Div(id='attic-output')
                                    ], className='attic-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'NEAR SCHOOL', style={'color':'#c86d53'}, className='school-title'
                                        ),
                                        html.Div(
                                            '(Gần Trường Học)', style={'color':'#c86d53'}, className='school-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='school',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='school-selected'
                                        ),
                                        html.Div(id='school-output')
                                    ], className='school-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'NEAR HOSPITAL', style={'color':'#c86d53'}, className='hospital-title'
                                        ),
                                        html.Div(
                                            '(Gần Bệnh Viện)', style={'color':'#c86d53'}, className='hospital-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='hospital',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='hospital-selected'
                                        ),
                                        html.Div(id='hospital-output')
                                    ], className='hospital-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'NEAR CENTER', style={'color':'#c86d53'}, className='center-title'
                                        ),
                                        html.Div(
                                            '(Gần Trung Tâm)', style={'color':'#c86d53'}, className='center-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='center',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='center-selected'
                                        ),
                                        html.Div(id='center-output')
                                    ], className='center-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'NEAR FRONTAGE', style={'color':'#c86d53'}, className='frontage-title'
                                        ),
                                        html.Div(
                                            '(Gần Mặt Tiền)', style={'color':'#c86d53'}, className='frontage-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='frontage',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='frontage-selected'
                                        ),
                                        html.Div(id='frontage-output')
                                    ], className='frontage-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'SERCURITY SPACE', style={'color':'#c86d53'}, className='security-title'
                                        ),
                                        html.Div(
                                            '(An Ninh Yên Tĩnh)', style={'color':'#c86d53'}, className='security-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='security',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='security-selected'
                                        ),
                                        html.Div(id='security-output')
                                    ], className='security-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'COMFORTABLE SPACE', style={'color':'#c86d53'}, className='comfortable-title'
                                        ),
                                        html.Div(
                                            '(Khu Vực Rộng Rãi)', style={'color':'#c86d53'}, className='comfortable-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='comfortable',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='comfortable-selected'
                                        ),
                                        html.Div(id='comfortable-output')
                                    ], className='comfortable-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'HAVE CAR PARK', style={'color':'#c86d53'}, className='car-title'
                                        ),
                                        html.Div(
                                            '(Chỗ Đậu Xe Rộng)', style={'color':'#c86d53'}, className='car-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='car',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='car-selected'
                                        ),
                                        html.Div(id='car-output')
                                    ], className='car-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'LARGER REAR', style={'color':'#c86d53'}, className='rear-title'
                                        ),
                                        html.Div(
                                            '(Nở Hậu)', style={'color':'#c86d53'}, className='rear-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='rear',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='rear-selected'
                                        ),
                                        html.Div(id='rear-output')
                                    ], className='rear-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'ALLEY SURFACE', style={'color':'#c86d53'}, className='surface-title'
                                        ),
                                        html.Div(
                                            '(Có Hẻm Thông)', style={'color':'#c86d53'}, className='surface-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='surface',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='surface-selected'
                                        ),
                                        html.Div(id='surface-output')
                                    ], className='surface-division'
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            'URGENT SALE', style={'color':'#c86d53'}, className='sale-title'
                                        ),
                                        html.Div(
                                            '(Cần Bán Gấp)', style={'color':'#c86d53'}, className='sale-title-vn'
                                        ),
                                        dcc.RadioItems(
                                            id='sale',
                                            options=(
                                                {'label': 'Yes', 'value': 1},
                                                {'label': 'No', 'value': 0},
                                            ),
                                            labelStyle={
                                                'cursor': 'pointer',
                                                'margin-left':'5px',
                                                'font-family':'Space Mono',
                                                
                                            },
                                            className='sale-selected'
                                        ),
                                        html.Div(id='sale-output')
                                    ], className='sale-division'
                                )
                            ], className='container-right-under-left'
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Button(
                                                    'ESTIMATE PRICE',
                                                    id='price-button',
                                                    n_clicks=0,
                                                    style={
                                                        'background-color': '#c86d53',
                                                        'color': '#f5ead0',
                                                        'width': '150px',
                                                        'height': '50px',
                                                        'font-family': 'Space Mono'
                                                    }
                                                ),
                                            ], className='button-clicked'
                                        ),
                                        html.Div(
                                            [
                                                html.Div(id='price-output',className='price-display')
                                            ], className='price-return'
                                        )
                                    ], className='price-division'
                                ),
                                html.Div(
                                    [
                                        html.H3(
                                            'PROJECT DESCRIPTION'
                                        ),
                                        html.P(
                                            [
                                                'This project is created by ',
                                                html.A(
                                                    '@caolong', href='https://www.facebook.com/liuliukiki/',target='_blank'
                                                ),
                                                ', 3rd-year student as FinTech major at ',
                                                html.A(
                                                    'University of Economics and Law', href='https://en.uel.edu.vn/',target='_blank'
                                                ),
                                                '. For more information and projects, visiting my ',
                                                html.A(
                                                    'Github', href='https://github.com/123olala',target='_blank'
                                                ),
                                                '.'
                                            ]
                                        ),
                                        html.P(
                                            [
                                                'The web app uses ML model to predict the house price in Ho Chi Minh City based on datasets are scraped from website ',
                                                html.A(
                                                    'Propzy', href='https://propzy.vn/',target='_blank'
                                                ),
                                                ' with more than 10,000 houses of districts in Ho Chi Minh City.'
                                            ]
                                        ),
                                        html.P(
                                            [
                                                'The algorithm (LightGBM) is built with a root mean square error of approximately 960 million VND.\
                                                    The R squared of model is also 95.7%.'
                                            ]
                                        )
                                    ], className='description-division'
                                )
                            ], className='container-right-under-right'
                        )
                    ], className='container-right-under'
                )
            ], className='container-right'
        )
    ], className='container'
)


#District input
@app.callback(
    Output('price-output', 'children'),
    Input('price-button','n_clicks'),
    [
        State('district', 'value'),
        State('category', 'value'),
        State('bedroom','value'),
        State('direction', 'value'),
        State('status', 'value'),
        State('verification', 'value'),
        State('area','value'),
        State('area-used','value'),
        State('width', 'value'),
        State('alley-width','value'),
        State('floor','value'),
        State('mezzanine','value'),
        State('rooftop','value'),
        State('basement', 'value'),
        State('attic', 'value'),
        State('school','value'),
        State('hospital', 'value'),
        State('center', 'value'),
        State('frontage', 'value'),
        State('security','value'),
        State('comfortable', 'value'),
        State('car', 'value'),
        State('rear', 'value'),
        State('surface', 'value'),
        State('sale','value')
    ]  
)
def return_price(
    button,district,category,bedroom,direction,status,verification,area,
    area_used,width,alley_width,floor,mezzanine,rooftop,basement,attic,
    school,hospital,center,frontage,securities,comfortable,
    car_park,larger_rear,alley_surface,urgent_sale
):
    #Load model
    model = joblib.load('final_model.sav')
    #Mapping category values
    district_dict = {
            'hoc-mon':0, 'binh-tan':7, 'nha-be':2, 'q11':12, 'thu-duc':10,
            'binh-chanh':1, 'binh-thanh':14, 'q3':19, 'q2':21, 'tan-phu':13,
            'q4':3, 'q12':5, 'tan-binh':16, 'q8':4, 'q10':9,
            'q6':11, 'q1':17, 'phu-nhuan':15, 'q9':6, 'q7':20,
            'go-vap':8, 'q5':18
            }
    category_dict = {
    'nha':1, 'can-ho':2, 'nha-mat-tien':4, 'day-tro':3, 'villa':5
}
    direction_dict = {
    'bac':3, 'tay':2, 'nam':4, 'khac':0, 'dong':1
}
    status_dict = {
    'de-trong':1, 'dang-o':2, 'dang-cho-thue':3, 'khac':0
}
    verification_dict = {
    'so-hong':2, 'khac':0, 'so-do':3, 'giay-chung-nhan-phuong':1
}

    #Create an array of features    
    input = np.array([
        button,district,category,bedroom,direction,status,verification,area,
        area_used,width,alley_width,floor,mezzanine,rooftop,basement,attic,
        school,hospital,center,frontage,securities,comfortable,
        car_park,larger_rear,alley_surface,urgent_sale
    ])

    if not button:
        pass
    else:
        if None in input:
            return 'You must select all attributes before clicking button'
        else:
            attributes = np.array([
                district_dict[district],category_dict[category],int(bedroom),direction_dict[direction],status_dict[status],
                verification_dict[verification],np.log(float(area)),np.log(float(area_used)),np.log(float(width)),np.log(float(alley_width)),
                int(floor),mezzanine,rooftop,basement,attic,school,hospital,center,frontage,securities,comfortable,car_park,
                larger_rear,alley_surface,urgent_sale
            ]).reshape(1,-1)
            #Estimate Price
            predicted_price = np.round(model.predict(attributes)[0],3)
            return f'Your house can be sold for approximately {predicted_price} billion VND'

if __name__ == '__main__':
    app.run_server()

    
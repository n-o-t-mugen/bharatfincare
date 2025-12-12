def get_dashboard_styles():
    # ========== CHANGE FONT HERE ==========
    FONT_NAME = "Urbanist"  # Options: Urbanist, Outfit, Lexend, Manrope, DM+Sans, Sora, Poppins, Josefin+Sans
    # ======================================
    
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family={FONT_NAME}:wght@100;200;300;400;500;600;700;800&display=swap');


        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}




        :root {{
            /* Company Colors */
            --primary-orange: #FF8C42;
            --dark-orange: #E67E22;
            --accent-green: #27AE60;
            --dark-green: #1E8449;
            --light-green: #52BE80;
            --white: #FFFFFF;
            --bg-light: #F9FAFB;
            --text-dark: #1A1A1A;
            --text-muted: #6C757D;
            
            /* Spacing & Sizing */
            --border-radius: 14px;
            --transition: 0.3s ease;
        }}




        html, body, [data-testid="stAppViewContainer"] {{
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            background: linear-gradient(135deg, #F9FAFB 0%, #FFF5F0 50%, #F0F5F2 100%) !important;
            font-family: '{FONT_NAME}', sans-serif !important;
            color: var(--text-dark);
            overflow: hidden !important;
        }}




        .main .block-container {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 0.8rem !important;
            height: 100vh !important;
            max-width: 100% !important;
            gap: 0 !important;
        }}




        /* ============ HEADER ============ */
        .dashboard-header {{
            background: linear-gradient(135deg, var(--primary-orange) 0%, var(--dark-orange) 100%);
            border-radius: var(--border-radius);
            padding: 0.6rem 1.5rem !important;
            text-align: center;
            position: relative;
            overflow: hidden;
            flex-shrink: 0;
            margin-bottom: 0.6rem !important;
            box-shadow: 0 8px 24px rgba(255, 140, 66, 0.25);
        }}




        .dashboard-header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.15), transparent 70%);
            border-radius: 50%;
            animation: float 8s ease-in-out infinite;
            z-index: 0;
        }}




        @keyframes float {{
            0%, 100% {{ transform: translate(0, 0); }}
            50% {{ transform: translate(15px, -15px); }}
        }}




        .dashboard-title {{
            font-family: '{FONT_NAME}', sans-serif;
            font-size: 1.35rem !important;
            font-weight: 800 !important;
            color: var(--white) !important;
            margin: 0 !important;
            letter-spacing: -0.5px;
            position: relative;
            z-index: 1;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}




        .dashboard-header p {{
            color: rgba(255, 255, 255, 0.92);
            font-weight: 500;
            font-size: 0.65rem !important;
            margin-top: 0.15rem !important;
            letter-spacing: 0.6px;
            position: relative;
            z-index: 1;
        }}




        /* ============ PROGRESS BAR SECTION ============ */
        .target-container {{
            background: linear-gradient(135deg, var(--white) 0%, #FAFAFA 100%);
            border: 1px solid #E8E8E8;
            border-radius: var(--border-radius);
            padding: 1rem 1.5rem !important;
            text-align: center;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
            flex-shrink: 0;
            margin-bottom: 0.7rem !important;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 0.8rem;
        }}




        .progress-label {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.2rem;
            width: 100%;
        }}




        .target-label {{
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.8px;
            font-size: 0.65rem !important;
            font-weight: 600;
            font-family: '{FONT_NAME}', sans-serif;
        }}




        .target-value {{
            font-family: '{FONT_NAME}', sans-serif;
            font-size: 1.3rem !important;
            background: linear-gradient(135deg, var(--primary-orange), var(--dark-orange));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            letter-spacing: -0.4px;
        }}




        /* ============ SIMPLE PROGRESS BAR ============ */
        .progress-wrapper {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            width: 100%;
            flex-wrap: wrap;
        }}




        .simple-progress-bar {{
            width: 100%;
            max-width: 600px;
            height: 24px;
            background: #E8E8E8;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
            position: relative;
        }}




        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #27AE60, #52BE80);
            border-radius: 12px;
            transition: width 0.6s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 20px rgba(39, 174, 96, 0.5);
            min-width: 45px;
        }}




        .percentage-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 800;
            font-size: 0.7rem !important;
            letter-spacing: -0.3px;
            font-family: '{FONT_NAME}', sans-serif;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        }}




        .percentage-display {{
            background: linear-gradient(135deg, var(--accent-green) 0%, var(--primary-orange) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 1rem !important;
            letter-spacing: -0.3px;
            font-family: '{FONT_NAME}', sans-serif;
            white-space: nowrap;
            flex-shrink: 0;
        }}




        /* ============ LEADERBOARD SECTION ============ */
        .leaderboard-container {{
            flex: 1;
            display: flex;
            flex-direction: column;
            min-height: 0;
            overflow: hidden;
        }}




        .leaderboard-title {{
            text-align: center;
            margin: 0 0 0.6rem 0 !important;
            flex-shrink: 0;
        }}




        .leaderboard-title h3 {{
            font-family: '{FONT_NAME}', sans-serif;
            background: linear-gradient(135deg, var(--primary-orange), var(--dark-orange));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.25rem !important;
            font-weight: 700;
            margin: 0 0 0.2rem 0 !important;
            letter-spacing: -0.5px;
        }}




        .leaderboard-subtitle {{
            color: var(--text-muted);
            font-size: 0.7rem !important;
            margin: 0 !important;
            font-weight: 500;
            letter-spacing: 0.3px;
            font-family: '{FONT_NAME}', sans-serif;
        }}




        /* ============ MANAGER CARDS ============ */
        .manager-card {{
            background: linear-gradient(135deg, var(--white) 0%, #FAFAFA 100%);
            border: 1px solid #E8E8E8;
            border-radius: var(--border-radius);
            padding: 1rem 0.8rem !important;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            transition: all var(--transition);
            cursor: pointer;
            flex: 1;
            overflow: hidden;
        }}




        .manager-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
            border-color: var(--primary-orange);
        }}




        .card-top {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            gap: 0.4rem;
        }}




        .manager-rank {{
            position: relative;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--white);
            font-weight: 900;
            font-size: 1.2rem !important;
            border: 4px solid var(--white);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
            z-index: 10;
            font-family: '{FONT_NAME}', sans-serif;
        }}




        .rank-1 {{ background: linear-gradient(135deg, #FFD700, #FFA500); }}
        .rank-2 {{ background: linear-gradient(135deg, #C0C0C0, #A8A8A8); }}
        .rank-3 {{ background: linear-gradient(135deg, #CD7F32, #A0522D); }}




        .manager-avatar {{
            width: 60px !important;
            height: 60px !important;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary-orange), var(--dark-orange));
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--white);
            font-size: 22px !important;
            font-weight: 800;
            box-shadow: 0 6px 18px rgba(255, 140, 66, 0.3);
            border: 3px solid var(--white);
            transition: transform var(--transition);
        }}




        .manager-card:hover .manager-avatar {{
            transform: scale(1.1);
        }}




        .manager-name {{
            font-family: '{FONT_NAME}', sans-serif;
            font-size: 0.85rem !important;
            font-weight: 700;
            color: var(--text-dark);
            margin: 0 !important;
            line-height: 1.2;
            word-wrap: break-word;
            letter-spacing: -0.3px;
            max-height: 2.2rem;
            overflow: hidden;
        }}




        .card-bottom {{
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }}




        .manager-amount {{
            font-family: '{FONT_NAME}', sans-serif;
            font-size: 1.1rem !important;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary-orange), var(--dark-orange));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 !important;
            letter-spacing: -0.4px;
        }}




        .manager-target {{
            font-size: 0.7rem !important;
            color: var(--text-muted);
            margin: 0 !important;
            font-weight: 600;
            background: linear-gradient(135deg, #F0F9F6, #FFF5F0);
            padding: 0.3rem 0.6rem !important;
            border-radius: 6px;
            border: 1px solid #E8E8E8;
            transition: all var(--transition);
            font-family: '{FONT_NAME}', sans-serif;
        }}




        .manager-card:hover .manager-target {{
            background: linear-gradient(135deg, var(--accent-green), var(--primary-orange));
            color: var(--white);
            border-color: transparent;
        }}




        /* ============ FOOTER ============ */
        .dashboard-footer {{
            text-align: center;
            color: var(--text-muted);
            font-size: 0.65rem !important;
            margin-top: 0.4rem !important;
            padding-top: 0.4rem !important;
            border-top: 1px solid #E8E8E8;
            font-weight: 600;
            letter-spacing: 0.3px;
            flex-shrink: 0;
            font-family: '{FONT_NAME}', sans-serif;
        }}




        ::-webkit-scrollbar {{ display: none !important; }}




        @media (max-width: 1200px) {{
            .dashboard-title {{ font-size: 1.25rem !important; }}
            .leaderboard-title h3 {{ font-size: 1.1rem !important; }}
            .manager-card {{ padding: 0.9rem 0.7rem !important; }}
            .manager-name {{ font-size: 0.8rem !important; }}
            .manager-amount {{ font-size: 1rem !important; }}
        }}




        @media (max-width: 768px) {{
            .simple-progress-bar {{
                max-width: 100%;
            }}
            .progress-wrapper {{
                flex-direction: column;
                gap: 0.8rem;
            }}
        }}
    </style>
    """
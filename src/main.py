from src.video_processing import process_video
from src.player_detection import detect_players
from src.tactical_analysis import analyze_tactics
from src.report_generator import generate_report

def main():
    video_path = 'data/raw_videos/partido_prueba.mp4'
    frames = process_video(video_path)
    players = detect_players(frames)
    analysis = analyze_tactics(players)
    generate_report(analysis)

if __name__ == '__main__':
    main()

import argparse
from Tools.ProgressServer import ProgressServer

def main():
    parser = argparse.ArgumentParser(description='进度控制脚本')
    parser.add_argument('--task-id', type=int, required=True, help='任务ID')
    parser.add_argument('--task-name', type=str, required=True, help='任务名称')
    parser.add_argument('--description', type=str, required=True, help='任务描述')
    parser.add_argument('--stage', type=str, required=True, 
                       choices=['started', 'milestone', 'completed', 'failed'], 
                       help='进度阶段')
    parser.add_argument('--tokens-used', type=int, required=True, help='已使用token数')
    parser.add_argument('--steps-used', type=int, required=True, help='已使用步骤数')
    parser.add_argument('--log', type=str, default='', help='操作日志')
    
    args = parser.parse_args()
    
    server = ProgressServer(args.task_id, args.task_name, args.description)
    server.update_progress(args.stage, args.tokens_used, args.steps_used, args.log)

if __name__ == "__main__":
    main()
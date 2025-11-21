"""
COBOL Code Executor mit GnuCOBOL
"""
import subprocess
import os
import tempfile

class CobolExecutor:
    def __init__(self):
        self.check_cobol_installed()
    
    def check_cobol_installed(self):
        try:
            result = subprocess.run(['cobc', '--version'], 
                                   capture_output=True, 
                                   text=True, 
                                   timeout=5)
            return result.returncode == 0
        except FileNotFoundError:
            return False
        except Exception:
            return False
    
    def execute_cobol(self, code):
        with tempfile.TemporaryDirectory() as tmpdir:
            source_file = os.path.join(tmpdir, 'program.cob')
            executable = os.path.join(tmpdir, 'program')
            
            try:
                with open(source_file, 'w') as f:
                    f.write(code)
                
                # Free-Format: Keine festen Spalten-Regeln!
                compile_result = subprocess.run(
                    ['cobc', '-x', '-free', source_file, '-o', executable],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if compile_result.returncode != 0:
                    return {
                        'success': False,
                        'output': '',
                        'error': self._format_compile_error(compile_result.stderr),
                        'stage': 'compilation'
                    }
                
                run_result = subprocess.run(
                    [executable],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                return {
                    'success': True,
                    'output': run_result.stdout,
                    'error': run_result.stderr if run_result.stderr else '',
                    'stage': 'execution'
                }
                
            except subprocess.TimeoutExpired:
                return {
                    'success': False,
                    'output': '',
                    'error': 'Timeout: Programm hat zu lange gedauert (max 5 Sekunden)',
                    'stage': 'execution'
                }
            except Exception as e:
                return {
                    'success': False,
                    'output': '',
                    'error': f'Fehler: {str(e)}',
                    'stage': 'unknown'
                }
    
    def _format_compile_error(self, error_msg):
        lines = error_msg.split('\n')
        formatted_lines = []
        
        for line in lines:
            if 'error:' in line.lower() or 'warning:' in line.lower():
                formatted_lines.append(line)
        
        if formatted_lines:
            return '\n'.join(formatted_lines)
        return error_msg

def install_cobol():
    try:
        print("Installiere GnuCOBOL...")
        subprocess.run(['apt-get', 'update'], check=True, capture_output=True)
        subprocess.run(['apt-get', 'install', '-y', 'gnucobol4'], 
                      check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"Installation fehlgeschlagen: {e}")
        return False

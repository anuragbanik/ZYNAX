export interface StudentProfile {
  name: string;
  email: string;
  branch: string;
  section: string;
  college: string;
  rollNumber?: string;
  targetAttendancePct: number;
}

export interface SubjectAttendance {
  id: string;
  name: string;
  attended: number;
  total: number;
  faculty: string;
  room: string;
}

export interface TimetablePeriod {
  time: string;
  subject: string;
  room: string;
  faculty: string;
  isNext?: boolean;
}

export interface ChapterProgress {
  unit: string;
  name: string;
  progress: number;
  topics: string;
}

export interface NoteItem {
  id: string;
  title: string;
  subject: string;
  content: string;
  createdAt: string;
}

export interface QuizQuestion {
  q: string;
  options: string[];
  answer: number;
  explanation: string;
}

export interface ApiErrorResponse {
   message?: string;
   error?: string;
   details?: string[];
}

export interface ApiSuccess<T> {
   data: T;
}

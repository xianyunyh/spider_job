import path from 'path';
import dotenv from 'dotenv';

/**
 * Load environment variables from .env* files
 */
function loadEnv() {
  // Adopt this convention https://github.com/bkeepers/dotenv#what-other-env-files-can-i-use
  // Inspired by https://pkg.go.dev/github.com/joho/godotenv#readme-precedence-conventions
  let appEnv = process.env.PLATFORM;
  if (!appEnv) {
    appEnv = 'production';
  }

  dotenv.config({
    path: path.resolve(process.cwd(), `.env.${appEnv}.local`),
  });
  if (appEnv != 'test') {
    dotenv.config({
      path: path.resolve(process.cwd(), '.env.local'),
    });
  }
  dotenv.config({
    path: path.resolve(process.cwd(), `.env.${appEnv}`),
  });

  // The Original .env
  dotenv.config();
}

export { loadEnv };

export class AuthorizationError extends Error {
  constructor(message) {
    super(message);
    this.name = "AuthorizationError";
  }
}

export class RegistrationError extends Error {
  constructor(message) {
    super(message);
    this.name = "RegistrationError";
  }
}